from django.db import models

class PointOfInterest(models.Model):
    # Common fields
    poi_id = models.CharField(max_length=255, blank=True, null=True)
    poi_name = models.CharField(max_length=255, blank=True, null=True)
    poi_category = models.CharField(max_length=255, blank=True, null=True)
    poi_latitude = models.FloatField(blank=True, null=True)
    poi_longitude = models.FloatField(blank=True, null=True)
    poi_ratings = models.TextField(blank=True, null=True)

    # Additional fields for JSON and XML
    poi_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.poi_name
