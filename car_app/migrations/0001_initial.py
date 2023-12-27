# Generated by Django 5.0 on 2023-12-25 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specification_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=20)),
                ('fuel', models.CharField(max_length=20)),
                ('top_speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_app.manufacturer_model')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_app.specification_model')),
            ],
        ),
    ]