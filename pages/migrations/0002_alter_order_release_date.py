# Generated by Django 5.0.7 on 2024-08-18 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 18, 13, 36, 55, 274105)),
        ),
    ]
