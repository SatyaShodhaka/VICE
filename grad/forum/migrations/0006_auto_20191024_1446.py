# Generated by Django 2.2.5 on 2019-10-24 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20191022_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 14, 46, 11, 305026)),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
