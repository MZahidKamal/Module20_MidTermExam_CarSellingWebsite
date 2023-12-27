# Generated by Django 5.0 on 2023-12-26 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0009_alter_car_model_model'),
        ('purchase_app', '0002_remove_purchase_model_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_model',
            name='model',
        ),
        migrations.AddField(
            model_name='purchase_model',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_app.car_model'),
        ),
    ]
