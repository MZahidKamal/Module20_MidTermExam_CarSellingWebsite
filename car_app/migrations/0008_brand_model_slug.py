# Generated by Django 5.0 on 2023-12-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0007_rename_post_comments_model_car_alter_car_model_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand_model',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]