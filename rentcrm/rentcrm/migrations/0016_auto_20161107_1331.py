# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcrm', '0015_auto_20161107_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
