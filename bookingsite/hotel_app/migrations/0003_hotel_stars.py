# Generated by Django 5.0.1 on 2024-06-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_remove_hotel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]
