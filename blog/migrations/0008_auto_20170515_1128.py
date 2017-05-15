# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[(b'EASY', 'easy'), (b'MEDIUM', 'normal'), (b'HARD', 'hard')], default=b'EASY', max_length=2),
        ),
    ]