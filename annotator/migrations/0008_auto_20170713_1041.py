# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0007_auto_20170713_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]