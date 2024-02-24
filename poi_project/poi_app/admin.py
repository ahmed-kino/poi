from django.contrib import admin
from .models import PointOfInterest

class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'poi_name', 'poi_external_id', 'poi_category', 'avg_rating')
    list_filter = ('poi_category',)
    search_fields = ('poi_name', 'poi_external_id')

admin.site.register(PointOfInterest, PointOfInterestAdmin)