# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rentcrm', '0017_auto_20161110_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='lease_term',
            field=models.IntegerField(choices=[(1, 'One year'), (2, 'Two years')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='security_deposit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='contract',
            name='signed_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]