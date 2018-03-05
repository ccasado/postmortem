# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Report(models.Model):
    date = models.DateField('Date')
    pub_date = models.DateTimeField('Date published')
    product = models.CharField(max_length=50, default='', verbose_name='Product')
    summary = models.CharField(max_length=100, default='', verbose_name='Summary')
    impact = models.TextField('Impact', default='')
    root_causes = models.TextField('Root causes', default='')
    trigger = models.CharField(max_length=100, default='', verbose_name='Trigger')
    resolution = models.TextField('Resolution', default='')
    detection = models.CharField(max_length=100, default='', verbose_name='Detection')

    def __str__(self):
        return self.summary

class Action(models.Model):
    MITIGATE = 'MIT'
    PREVENT = 'PREV'
    PROCESS = 'PROC'
    OTHER = 'OTH'
    ACTION_TYPE_CHOICES = (
        (MITIGATE, 'mitigate'),
        (PREVENT, 'prevent'),
        (PROCESS, 'process'),
        (OTHER, 'other')
    )
    report = models.ForeignKey(Report, on_delete=models.CASCADE, default='')
    item = models.CharField(max_length=100, default='', verbose_name='Item')
    action_type = models.CharField(max_length=50, choices=ACTION_TYPE_CHOICES, default='other', verbose_name='Type')

    def __str__(self):
        return self.item
