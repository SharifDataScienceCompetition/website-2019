# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-02-26 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0046_teamparticipateschallenge_payment_time_remained'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamparticipateschallenge',
            name='payment_time_remained',
        ),
        migrations.AddField(
            model_name='challenge',
            name='invited_to_ranking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teamparticipateschallenge',
            name='has_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teamparticipateschallenge',
            name='payment_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
