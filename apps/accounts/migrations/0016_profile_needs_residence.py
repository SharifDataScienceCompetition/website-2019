# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-02-26 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190225_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='needs_residence',
            field=models.BooleanField(default=False),
        ),
    ]