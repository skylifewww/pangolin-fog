# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20170208_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='related_category',
        ),
        migrations.AddField(
            model_name='product',
            name='related_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='related', related_query_name='related', to='product.Category', verbose_name='Related Category'),
        ),
    ]
