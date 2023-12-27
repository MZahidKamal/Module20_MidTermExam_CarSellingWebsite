# Generated by Django 5.0 on 2023-12-26 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0009_alter_car_model_model'),
        ('purchase_app', '0004_alter_purchase_model_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_model',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_purchases_model', to='car_app.car_model'),
        ),
        migrations.AlterField(
            model_name='purchase_model',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_purchases_model', to='car_app.car_model'),
        ),
    ]
