from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all_by_property/', views.get_all_by_property, name='get_all_by_property'),
    path('ingest/single', views.ingest_single, name='ingest_single'),
    path('ingest/batch', views.ingest_batch, name='ingest_batch')
]