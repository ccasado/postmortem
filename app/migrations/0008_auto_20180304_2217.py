# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_action_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='product',
            field=models.CharField(default='', max_length=50, verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='action',
            name='item',
            field=models.CharField(default='', max_length=100, verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='report',
            name='detection',
            field=models.CharField(default='', max_length=100, verbose_name='Detection'),
        ),
        migrations.AlterField(
            model_name='report',
            name='impact',
            field=models.CharField(default='', max_length=100, verbose_name='Impact'),
        ),
        migrations.AlterField(
            model_name='report',
            name='resolution',
            field=models.TextField(default='', verbose_name='Resolution'),
        ),
        migrations.AlterField(
            model_name='report',
            name='root_causes',
            field=models.TextField(default='', verbose_name='Root causes'),
        ),
        migrations.AlterField(
            model_name='report',
            name='summary',
            field=models.CharField(default='', max_length=100, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='report',
            name='trigger',
            field=models.CharField(default='', max_length=100, verbose_name='Trigger'),
        ),
    ]
