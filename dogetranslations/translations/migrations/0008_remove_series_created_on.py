# Generated by Django 4.2.7 on 2023-11-17 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("translations", "0007_series_created_on"),
    ]

    operations = [
        migrations.RemoveField(model_name="series", name="created_on",),
    ]
