# Generated by Django 4.0.3 on 2022-03-17 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_alter_reports_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='locations',
        ),
        migrations.AddField(
            model_name='reports',
            name='locations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scraper.locations'),
        ),
    ]
