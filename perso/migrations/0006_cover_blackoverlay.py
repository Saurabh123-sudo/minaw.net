# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perso', '0005_auto_20170705_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='blackOverlay',
            field=models.BooleanField(default=False, verbose_name='surimpression noire'),
        ),
    ]
