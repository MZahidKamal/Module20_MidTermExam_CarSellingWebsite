# Generated by Django 5.0 on 2023-12-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_app', '0002_remove_car_model_manufacturer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=20)),
                ('fuel', models.CharField(max_length=20)),
                ('top_speed', models.IntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
