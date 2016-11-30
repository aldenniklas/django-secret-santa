# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_santa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santa',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='santa',
            name='restrictions',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='santa',
            name='wishlist',
            field=models.TextField(blank=True),
        ),
    ]
