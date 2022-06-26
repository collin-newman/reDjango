from django.urls import path
from . import views

urlpatterns = [
    path('get_all_properties', views.get_all_properties, name='get_all_properties'),
    path('filter_all_by_attribute/', views.filter_all_by_attribute, name='filter_all_by_attribute'),
    path('ingest/single', views.ingest_single, name='ingest_single'),
    path('ingest/batch', views.ingest_batch, name='ingest_batch')
]