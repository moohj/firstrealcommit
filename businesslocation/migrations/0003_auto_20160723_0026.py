# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesslocation', '0002_auto_20160717_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstrace',
            name='country',
            field=models.CharField(default='United States', max_length=120),
        ),
        migrations.AlterField(
            model_name='businesstrace',
            name='latitude',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='businesstrace',
            name='longitude',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='businesstrace',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
