# Generated by Django 5.0 on 2023-12-26 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0009_alter_car_model_model'),
        ('purchase_app', '0005_purchase_model_price_alter_purchase_model_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase_model',
            name='price',
        ),
        migrations.AlterField(
            model_name='purchase_model',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_app.car_model'),
        ),
        migrations.AddField(
            model_name='purchase_model',
            name='payment_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase_app.paymentmethods_model'),
        ),
    ]