# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-29 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=160),
        ),
    ]
