from django.db import models
from django.contrib.gis.db import models

# TODO change all integar models over to Floats that deal with money

# Create your models here.
class Properties(models.Model):
    # Primary Key
    full_address = models.CharField(max_length=300, default='', primary_key=True)
    # Location data
    address_line_1 = models.CharField(max_length=200, default='')
    address_line_2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=30, default='')
    zipcode = models.SmallIntegerField(default=None)
    neighborhood = models.CharField(max_length=200, default='')
    lat = models.FloatField(default=None)
    lon = models.FloatField(default=None)
    point = models.PointField(null=True)
    # General Info
    property_type = models.CharField(max_length=30, default='')
    septic_tank = models.BooleanField(default=False)
    garage_spaces = models.SmallIntegerField(default=None)
    property_sub_type = models.CharField(max_length=30, defualt='')
    septic_tank = models.BooleanField(default=False)
    garage_spaces = models.SmallIntegerField(default=None)
    last_updated_date = models.DateTimeField(default=None)
    list_date: models.DateTimeField(default=None)
    us_real_estate_api_id = models.CharField(max_length=20, default='')
    is_new_construction = models.BooleanField(default=False)
    is_subdivision = models.BooleanField(default=False)
    is_plan = models.BooleanField(default=False)
    is_price_reduced = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=False)
    is_foreclosure = models.BooleanField(default=False)
    is_new_listing = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    is_contingent = models.BooleanField(default=False)

    year_built = models.SmallIntegerField(default=None)
    baths_3qtr: models.SmallIntegerField(default=None)
    sold_date: models.DateField(default=None)
    sold_price: models.SmallIntegerField(default=None)
    baths_full: models.SmallIntegerField(default=None)
    baths_half: models.SmallIntegerField(default=None)
    lot_sqft: models.SmallIntegerField(default=None)
    sqft: models.SmallIntegerField(default=None)
    baths: models.SmallIntegerField(default=None)
    baths_1qtr: models.SmallIntegerField(default=None)
    stories: models.SmallIntegerField(default=None)
    beds: models.SmallIntegerField(default=None)

    # Purchase Info
    purchase_price = models.IntegerField(default=None)
    rehab_costs = models.IntegerField(default=None)
    down_payment = models.IntegerField(default=None)
    loan_amount = models.IntegerField(default=None)
    closing_costs = models.IntegerField(default=None)
    equity_required = models.IntegerField(default=None)
    mortgage_payment = models.SmallIntegerField(default=None)
    mortgage_rate = models.FloatField(default=None)

    # Income
    rent = models.SmallIntegerField(default=None)
    rent_after_vacancy = models.SmallIntegerField(default=None)
    effective_gross_income = models.SmallIntegerField(default=None)
    net_operating_income = models.SmallIntegerField(default=None)
    net_cash_flow = models.SmallIntegerField(default=None)

    # Operating Expenses
    property_tax = models.SmallIntegerField(default=None)
    hoa = models.SmallIntegerField(default=None)
    property_management = models.SmallIntegerField(default=None)
    home_insurance = models.SmallIntegerField(default=None)
    monthly_repairs = models.SmallIntegerField(default=None)
    monthly_capex = models.SmallIntegerField(default=None)
    total_monthly_expenses = models.SmallIntegerField(default=None)

    # Metrics
    cap_rate = models.FloatField(default=None)
    cash_on_cash = models.FloatField(default=None)
