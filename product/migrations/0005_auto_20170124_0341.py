# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-24 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_overview_slideproduct_techspec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='product',
        ),
        migrations.AddField(
            model_name='overview',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='overcat', to='product.Category', verbose_name='Category'),
        ),
    ]
