# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcrm', '0029_auto_20161125_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaserenewaloffer',
            name='is_sent',
            field=models.BooleanField(default=True, verbose_name='Sent'),
        ),
    ]