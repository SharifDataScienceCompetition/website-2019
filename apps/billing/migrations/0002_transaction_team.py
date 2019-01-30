# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-30 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='game.TeamParticipatesChallenge'),
        ),
    ]