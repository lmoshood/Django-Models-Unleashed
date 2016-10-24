# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 21:59
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161024_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.EmailField(blank=True, max_length=240, null=True, validators=[blog.validators.validate_justin]),
        ),
    ]