# Generated by Django 4.2.5 on 2023-12-14 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulancebooking',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 14, 10, 29, 18, 15343)),
        ),
    ]