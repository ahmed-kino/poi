from django.db import models

class PointOfInterest(models.Model):
    # Common fields
    poi_external_id = models.CharField(max_length=255, unique=True)
    poi_name = models.CharField(max_length=255, blank=True, null=True)
    poi_category = models.CharField(max_length=255, blank=True, null=True)
    poi_latitude = models.FloatField(blank=True, null=True)
    poi_longitude = models.FloatField(blank=True, null=True)
    poi_ratings = models.TextField(blank=True, null=True)

    # Additional fields for JSON and XML
    poi_description = models.TextField(blank=True, null=True, db_index=True)

    # Additional fields for external ID and average rating
    avg_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.poi_name

    def save(self, *args, **kwargs):
        if self.poi_ratings:
            try:
                ratings = [float(rating) for rating in  self.poi_ratings.strip('{}').split(',')]
                avg_rating = sum(ratings) / len(ratings) if ratings else None
                self.avg_rating = avg_rating
            except Exception as e:
                raise Exception(f'Error saving average rating in the db {e}')
        super().save(*args, **kwargs)