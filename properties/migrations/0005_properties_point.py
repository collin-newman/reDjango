# Generated by Django 4.0.5 on 2022-06-26 19:38

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_rename_long_properties_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]