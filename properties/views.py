from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from properties.models import Properties

# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse(Properties.objects.all().values())

@csrf_exempt
def get_all_by_property(request):
    body = json.loads(request.body)
    request_filters = {}
    for key in body:
        request_filters[key] = body[key]
    print(request_filters)
    return HttpResponse(Properties.objects.filter(**request_filters).values())