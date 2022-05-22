from bdb import effective
from django.db import models

# Create your models here.
class Properties(models.Model):
    # General Info
    state: models.CharField(max_length=30)
    zipcode: models.SmallIntegerField()
    neighborhood: models.CharField(max_length=200)
    lat: models.FloatField()
    long: models.FloatField()
    property_type: models.CharField(max_length=30)
    septic_tank: models.BooleanField(default=False)
    garage_spaces: models.SmallIntegerField()

    # Purchase Info
    purchase_price: models.SmallIntegerField()
    rehab_costs: models.SmallIntegerField()
    down_payment: models.SmallIntegerField()
    loan_amount: models.SmallIntegerField()
    closing_costs: models.SmallIntegerField()
    equity_required: models.SmallIntegerField()
    mortgage: models.SmallIntegerField()
    mortgate_rate: models.FloatField()

    # Income
    rent: models.SmallIntegerField()
    rent_after_vacancy: models.SmallIntegerField()
    effective_gross_income: models.SmallIntegerField()
    net_cash_flow: models.SmallIntegerField()

    # Operating Expenses
    property_tax: models.SmallIntegerField()
    hoa: models.SmallIntegerField()
    property_management: models.SmallIntegerField()
    home_insurance: models.SmallIntegerField()
    monthly_repairs: models.SmallIntegerField()
    monthly_capex: models.SmallIntegerField()

    # Metrics
    cap_rate: models.FloatField()
    cash_on_cash: models.FloatField()

    