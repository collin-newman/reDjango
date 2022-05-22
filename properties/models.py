from django.db import models

# Create your models here.
class Properties(models.Model):
    # General Info
    state = models.CharField(max_length=30, default='')
    zipcode = models.SmallIntegerField(default=None)
    neighborhood = models.CharField(max_length=200, default='')
    lat = models.FloatField(default=None)
    long = models.FloatField(default=None)
    property_type = models.CharField(max_length=30, default='')
    septic_tank = models.BooleanField(default=False)
    garage_spaces = models.SmallIntegerField(default=None)

    # Purchase Info
    purchase_price = models.IntegerField(default=None)
    rehab_costs = models.IntegerField(default=None)
    down_payment = models.IntegerField(default=None)
    loan_amount = models.IntegerField(default=None)
    closing_costs = models.IntegerField(default=None)
    equity_required = models.IntegerField(default=None)
    mortgage = models.SmallIntegerField(default=None)
    mortgate_rate = models.FloatField(default=None)

    # Income
    rent = models.SmallIntegerField(default=None)
    rent_after_vacancy = models.SmallIntegerField(default=None)
    effective_gross_income = models.SmallIntegerField(default=None)
    net_cash_flow = models.SmallIntegerField(default=None)

    # Operating Expenses
    property_tax = models.SmallIntegerField(default=None)
    hoa = models.SmallIntegerField(default=None)
    property_management = models.SmallIntegerField(default=None)
    home_insurance = models.SmallIntegerField(default=None)
    monthly_repairs = models.SmallIntegerField(default=None)
    monthly_capex = models.SmallIntegerField(default=None)

    # Metrics
    cap_rate = models.FloatField(default=None)
    cash_on_cash = models.FloatField(default=None)

    