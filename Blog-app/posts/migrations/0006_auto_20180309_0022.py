# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-09 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20180307_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='longitude',
            field=models.IntegerField(default=0),
        ),
    ]
