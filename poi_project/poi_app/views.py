from django.views.generic import ListView, DetailView
from .models import PointOfInterest

class PoiListView(ListView):
    model = PointOfInterest

class PoiDetailView(DetailView):
    model = PointOfInterest
