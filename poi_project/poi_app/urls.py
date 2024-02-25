from django.urls import path

from . import views

urlpatterns = [
    path('poi/', views.PoiListView.as_view(), name='poi_list'),
    path('poi/<int:pk>/', views.PoiDetailView.as_view(), name='poi_detail'),
]
