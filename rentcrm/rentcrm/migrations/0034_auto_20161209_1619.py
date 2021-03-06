# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcrm', '0033_auto_20171128_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='tenant',
        ),
        migrations.AddField(
            model_name='contract',
            name='main_tenant_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contract',
            name='tenants',
            field=models.ManyToManyField(to='rentcrm.Tenant'),
        ),
    ]
