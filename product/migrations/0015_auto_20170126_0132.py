# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-26 01:32
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20170126_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='slogan',
            field=models.CharField(max_length=250, verbose_name='Accessory Slogan'),
        ),
    ]