# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-29 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('u', 'unknown'), ('v', 'valid'), ('c', 'cancelled')], max_length=1)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('reference_id', models.CharField(max_length=100)),
                ('id2', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('error', models.CharField(blank=True, max_length=100, null=True)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='game.TeamParticipatesChallenge')),
            ],
        ),
    ]
