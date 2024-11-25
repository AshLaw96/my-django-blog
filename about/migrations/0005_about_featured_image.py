# Generated by Django 4.2.16 on 2024-11-25 10:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_collaboraterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
