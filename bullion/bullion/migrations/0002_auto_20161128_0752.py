# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bullion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(max_length=500, upload_to=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='reader_legal_status',
            field=models.CharField(choices=[('INDIV', 'Individual'), ('ENTIT', 'Entity'), ('NOTSP', 'Not specified')], max_length=5),
        ),
    ]
