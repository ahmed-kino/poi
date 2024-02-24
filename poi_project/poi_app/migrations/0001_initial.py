# Generated by Django 5.0.2 on 2024-02-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poi_external_id', models.CharField(max_length=255, unique=True)),
                ('poi_name', models.CharField(blank=True, max_length=255, null=True)),
                ('poi_category', models.CharField(blank=True, max_length=255, null=True)),
                ('poi_latitude', models.FloatField(blank=True, null=True)),
                ('poi_longitude', models.FloatField(blank=True, null=True)),
                ('poi_ratings', models.TextField(blank=True, null=True)),
                ('poi_description', models.TextField(blank=True, db_index=True, null=True)),
                ('avg_rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
