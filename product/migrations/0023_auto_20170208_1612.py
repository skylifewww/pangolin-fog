# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-08 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20170204_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_small',
            field=models.CharField(blank=True, max_length=250, verbose_name='Slug_Small'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=250, verbose_name='Slug'),
        ),
    ]
