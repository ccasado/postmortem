# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180305_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='impact',
            field=models.TextField(default='', help_text='help i need somebody', verbose_name='Impact'),
        ),
    ]
