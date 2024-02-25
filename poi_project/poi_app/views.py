from django.views.generic import DetailView, ListView

from .models import PointOfInterest


class PoiListView(ListView):
    model = PointOfInterest


class PoiDetailView(DetailView):
    model = PointOfInterest
