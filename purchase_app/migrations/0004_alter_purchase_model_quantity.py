# Generated by Django 5.0 on 2023-12-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0003_remove_purchase_model_model_purchase_model_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_model',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
