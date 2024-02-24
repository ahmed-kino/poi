import csv
import json
import logging
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from django.core.management.base import BaseCommand
from poi_app.models import PointOfInterest
import mimetypes

class Command(BaseCommand):
    help = 'Import PoI data from CSV, JSON, and XML files'

    def add_arguments(self, parser):
        parser.add_argument('file_paths', nargs='+', type=str, help='List of paths to the files to import')
        parser.add_argument('--log_file', type=str, help='Path to the log file')

    def handle(self, *args, **kwargs):
        file_paths = kwargs['file_paths']
        log_file = kwargs.get('log_file')

        logging.basicConfig(filename=log_file, level=logging.DEBUG)

        for file_path in file_paths:
            self.import_data(file_path)

    def import_data(self, file_path):
        file_type = self.detect_file_type(file_path)

        if file_type == 'csv':
            self.import_csv(file_path)
        elif file_type == 'json':
            self.import_json(file_path)
        elif file_type == 'xml':
            self.import_xml(file_path)
        else:
            self.stdout.write(self.style.ERROR(f'Unsupported file type: {file_type}'))

    def detect_file_type(self, file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        return mime_type.split('/')[1]

    def import_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        def process_row(row):
            try:
                poi = PointOfInterest.objects.create(
                    poi_external_id=row['poi_id'],
                    poi_name=row['poi_name'],
                    poi_category=row['poi_category'],
                    poi_latitude=float(row['poi_latitude']),
                    poi_longitude=float(row['poi_longitude']),
                    poi_ratings=row['poi_ratings']
                )
                self.stdout.write(self.style.SUCCESS(f'Imported PoI: {poi}'))
            except Exception as e:
                error_message = f'Invalid data: {e} --> Row: {row}'
                self.stdout.write(self.style.ERROR(error_message))
                logging.warning(error_message)

        with ThreadPoolExecutor() as executor:
            executor.map(process_row, rows)

    def import_json(self, file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                try:
                    poi = PointOfInterest.objects.create(
                        poi_id=item['id'],
                        poi_name=item['name'],
                        poi_category=item['category'],
                        description=item.get('description'),
                        poi_latitude=float(item['coordinates']['latitude']),
                        poi_longitude=float(item['coordinates']['longitude']),
                        poi_ratings=json.dumps(item['ratings'])
                    )
                    self.stdout.write(self.style.SUCCESS(f'Imported PoI: {poi}'))
                except Exception as e:
                    logging.warning(f'Invalid data: {e} --> Item: {item}')

    def import_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        for item in root.findall('DATA_RECORD'):
            try:
                poi = PointOfInterest.objects.create(
                    poi_id=item.find('pid').text,
                    poi_name=item.find('pname').text,
                    poi_category=item.find('pcategory').text,
                    poi_latitude=float(item.find('platitude').text),
                    poi_longitude=float(item.find('plongitude').text),
                    poi_ratings=item.find('pratings').text
                )
                self.stdout.write(self.style.SUCCESS(f'Imported PoI: {poi}'))
            except Exception as e:
                logging.warning(f'Invalid data: {e} --> Item: {item}')
