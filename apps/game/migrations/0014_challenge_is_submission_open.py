# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-04 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_auto_20180203_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='is_submission_open',
            field=models.BooleanField(default=False),
        ),
    ]
