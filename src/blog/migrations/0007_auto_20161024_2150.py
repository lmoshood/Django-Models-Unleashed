# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161024_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=240, unique=True, verbose_name='Post title'),
        ),
    ]
