# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_category_published_in_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_title',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Related Product Title'),
        ),
    ]