# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='rent_for_garage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
