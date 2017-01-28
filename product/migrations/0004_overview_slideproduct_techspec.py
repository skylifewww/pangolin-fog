# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-24 03:35
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170112_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name='Url')),
                ('published', models.BooleanField(verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name_plural': 'Overviews',
                'db_table': 'overviews',
                'verbose_name': 'Overview',
            },
        ),
        migrations.CreateModel(
            name='SlideProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name='Url pic')),
                ('text1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text1')),
                ('text2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text2')),
                ('published', models.BooleanField(verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='product.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Slides',
                'verbose_name': 'Slide',
            },
        ),
        migrations.CreateModel(
            name='TechSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('text1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text1')),
                ('text2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text2')),
                ('text3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Text3')),
                ('published', models.BooleanField(verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name_plural': 'TechSpecs',
                'db_table': 'techSpecs',
                'verbose_name': 'TechSpec',
            },
        ),
    ]