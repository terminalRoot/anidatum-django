# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0009_auto_20170713_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='source',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
