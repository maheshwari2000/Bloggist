# Generated by Django 3.0.3 on 2020-09-18 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200918_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 17, 10, 42, 805143, tzinfo=utc)),
        ),
    ]
