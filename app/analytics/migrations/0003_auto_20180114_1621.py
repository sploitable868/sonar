# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-14 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20180114_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='range_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='range_start',
            field=models.DateTimeField(),
        ),
    ]
