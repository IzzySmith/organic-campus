# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170404_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to=b'static/img/', verbose_name=b'figure'),
        ),
    ]
