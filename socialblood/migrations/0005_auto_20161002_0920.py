# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialblood', '0004_auto_20161002_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
