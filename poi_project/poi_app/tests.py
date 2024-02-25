from django.test import TestCase
from .models import PointOfInterest

POI_EXTERNAL_ID='1234'
POI_NAME='TEST POI'
POI_CATEGORY='TEST CATEGORY'
POI_LATITUDE=40.1234
POI_LONGITUDE=-74.1234

class PointOfInterestTestCase(TestCase):
    def test_save_valid_ratings(self):
        poi = PointOfInterest.objects.create(
            poi_external_id=POI_EXTERNAL_ID,
            poi_name=POI_NAME,
            poi_category=POI_CATEGORY,
            poi_latitude=POI_LATITUDE,
            poi_longitude=POI_LONGITUDE,
            poi_ratings='{3.0,4.0,3.0,5.0,2.0,3.0,2.0,2.0,2.0,2.0}'
        )
        self.assertEqual(poi.avg_rating, 2.8)

    def test_save_invalid_ratings(self):
        with self.assertRaises(Exception) as context:
            PointOfInterest.objects.create(
                poi_external_id=POI_EXTERNAL_ID,
                poi_name=POI_NAME,
                poi_category=POI_CATEGORY,
                poi_latitude=POI_LATITUDE,
                poi_longitude=POI_LONGITUDE,
                poi_ratings='{3.0,4.0,invalid,5.0,2.0,3.0,2.0,2.0,2.0,2.0}'
            )
        self.assertTrue('Error saving average rating in the db' in str(context.exception))


    def test_save_no_ratings(self):
        poi = PointOfInterest.objects.create(
            poi_external_id=POI_EXTERNAL_ID,
            poi_name=POI_NAME,
            poi_category=POI_CATEGORY,
            poi_latitude=POI_LATITUDE,
            poi_longitude=POI_LONGITUDE,
            poi_ratings=''
        )
        self.assertIsNone(poi.avg_rating)