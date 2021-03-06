# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-02-11 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0044_auto_20190210_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileuploadquestion',
            name='score2',
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='score2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trial',
            name='score2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='model_name',
            field=models.CharField(choices=[('Question', 'Question'), ('IntervalQuestion', 'IntervalQuestion'), ('FileUploadQuestion', 'FileUploadQuestion'), ('MultipleAnswerQuestion', 'MultipleAnswerQuestion'), ('MultipleChoiceQuestion', 'MultipleChoiceQuestion'), ('CodeUploadQuestion', 'CodeUploadQuestion')], max_length=200),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='type',
            field=models.CharField(blank=True, choices=[('multiple_choice', 'multiple_choice'), ('single_answer', 'single_answer'), ('multiple_answer', 'multiple_answer'), ('single_sufficient_answer', 'single_sufficient_answer'), ('single_number', 'single_number'), ('interval_number', 'interval_number'), ('file_upload', 'file_upload'), ('code_upload', 'code_upload')], max_length=200, null=True),
        ),
    ]
