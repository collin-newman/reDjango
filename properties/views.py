from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.gis.geos import Point
from django.db import connection
from django.http import JsonResponse
from properties.models import Properties

# Create your views here.


@csrf_exempt
def get_all_properties(request):
    all_records = []
    for property in Properties.objects.all().values():
        property["point"] = property["point"].wkt
        all_records.append(property)

    return JsonResponse(all_records, safe=False)


@csrf_exempt
def filter_all_by_attribute(request):
    body = json.loads(request.body)
    request_filters = {}
    for key in body:
        request_filters[key] = body[key]
    print(request_filters)
    return HttpResponse(Properties.objects.filter(**request_filters).values())


@csrf_exempt
def ingest_single(request):
    body = json.loads(request.body)
    full_address = ','.join([
        body['address_line_1'],
        body['address_line_2'],
        body['city'],
        body['state'],
    ])

    new_property = Properties.objects.create(
        full_address=full_address,
        address_line_1=body['address_line_1'],
        address_line_2=body['address_line_2'],
        city=body['city'],
        state=body['state'],
        zipcode=body['zipcode'],
        neighborhood=body['neighborhood'],
        lat=body['lat'],
        lon=body['lon'],
        point=Point(body['lat'], body['lon']),
        property_type=body['property_type'],
        septic_tank=body['septic_tank'],
        garage_spaces=body['garage_spaces'],
        purchase_price=body['purchase_price'],
        rehab_costs=body['rehab_costs'],
        down_payment=body['down_payment'],
        loan_amount=body['loan_amount'],
        closing_costs=body['closing_costs'],
        equity_required=body['equity_required'],
        mortgage=body['mortgage'],
        mortgage_rate=body['mortgage_rate'],
        rent=body['rent'],
        rent_after_vacancy=body['rent_after_vacancy'],
        effective_gross_income=body['effective_gross_income'],
        net_cash_flow=body['net_cash_flow'],
        property_tax=body['property_tax'],
        hoa=body['hoa'],
        property_management=body['property_management'],
        home_insurance=body['home_insurance'],
        monthly_repairs=body['monthly_repairs'],
        monthly_capex=body['monthly_capex'],
        cap_rate=body['cap_rate'],
        cash_on_cash=body['cash_on_cash']
    )

    new_property.save()
    print(f'Ingesting: {full_address}')
    return HttpResponse(f'Ingesting: {full_address}', content_type='application/json')


@csrf_exempt
def ingest_batch(request):
    body = json.loads(request.body)

    return HttpResponse('batch recored endpoint')


@csrf_exempt
def polygon_search(request):
    body = json.loads(request.body)
    geo_polygon = body['geo_polygon']
    polygon_query = f"""
        SELECT *
        FROM properties_properties
        WHERE ST_Contains(ST_GEOMFROMTEXT('SRID=4326;
            {geo_polygon}
        '), properties_properties.POINT);
    """
    cursor = connection.cursor()
    cursor.execute(polygon_query)
    properties = cursor.fetchall()
    return HttpResponse(properties)
