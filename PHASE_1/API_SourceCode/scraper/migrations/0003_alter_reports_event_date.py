# Generated by Django 4.0.3 on 2022-03-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_alter_locations_country_alter_locations_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='event_date',
            field=models.DateTimeField(blank=True, db_column='event_date', null=True),
        ),
    ]