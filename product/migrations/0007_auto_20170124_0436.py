# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-24 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20170124_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='category',
        ),
        migrations.AddField(
            model_name='overview',
            name='product',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='overprod', to='product.Product', verbose_name='Product'),
        ),
    ]
