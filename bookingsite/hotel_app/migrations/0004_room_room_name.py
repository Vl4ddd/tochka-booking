# Generated by Django 5.0.1 on 2024-06-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_hotel_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default='Обычный номер', max_length=255),
        ),
    ]
