# Generated by Django 4.0.5 on 2022-06-26 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_rename_mortgate_rate_properties_mortgage_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='long',
            new_name='lon',
        ),
    ]
