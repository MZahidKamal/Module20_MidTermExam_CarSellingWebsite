# Generated by Django 5.0 on 2023-12-25 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_model',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='car_model',
            name='specification',
        ),
        migrations.DeleteModel(
            name='Manufacturer_Model',
        ),
        migrations.DeleteModel(
            name='Car_Model',
        ),
        migrations.DeleteModel(
            name='Specification_Model',
        ),
    ]
