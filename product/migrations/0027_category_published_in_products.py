# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-12 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20170211_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='published_in_products',
            field=models.BooleanField(default='', verbose_name='Published in all products'),
        ),
    ]
