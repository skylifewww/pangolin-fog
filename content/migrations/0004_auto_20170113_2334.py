# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-13 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20170113_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='header_about',
            field=models.BooleanField(default='', verbose_name='About'),
        ),
        migrations.AddField(
            model_name='slide',
            name='published_news',
            field=models.BooleanField(default='', verbose_name='News'),
        ),
    ]
