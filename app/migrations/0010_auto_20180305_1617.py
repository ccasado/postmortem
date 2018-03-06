# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180304_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='owner',
            field=models.CharField(default='', max_length=50, verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='report',
            name='authors',
            field=models.CharField(default='', max_length=100, verbose_name='Authors'),
        ),
        migrations.AlterField(
            model_name='action',
            name='action_type',
            field=models.CharField(choices=[('MIT', 'mitiga\xe7\xe3o'), ('PREV', 'preven\xe7\xe3o'), ('PROC', 'processo'), ('OTH', 'outro')], default='other', max_length=50, verbose_name='Type'),
        ),
    ]