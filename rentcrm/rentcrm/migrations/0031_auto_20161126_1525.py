# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentcrm', '0030_auto_20161125_0602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractcondition',
            options={'verbose_name': 'Lease period', 'verbose_name_plural': 'Lease periods'},
        ),
    ]
