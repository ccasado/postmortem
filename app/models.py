# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Report(models.Model):
    date = models.DateField('Date')
    pub_date = models.DateTimeField('Date published')
    product = models.CharField(max_length=50, default='', verbose_name='Product')
    authors = models.CharField(max_length=100, default='', verbose_name='Authors')
    summary = models.CharField(max_length=100, default='', verbose_name='Summary')
    impact = models.TextField('Impact', default='', help_text='Efeito sobre o usuário final ou ao negócio.')
    root_causes = models.TextField('Root causes', default='', help_text='Explicação sobre as circunstâncias em que o incidente ocorreu. Pode ser útil usar a técnica 5 Whys.')
    trigger = models.CharField(max_length=100, default='', verbose_name='Trigger', blank=True)
    resolution = models.TextField('Resolution', default='')
    detection = models.CharField(max_length=100, default='', verbose_name='Detection', blank=True)

    def __str__(self):
        return self.summary

class Action(models.Model):
    MITIGATE = 'MIT'
    PREVENT = 'PREV'
    PROCESS = 'PROC'
    OTHER = 'OTH'
    ACTION_TYPE_CHOICES = (
        (MITIGATE, 'mitigação'),
        (PREVENT, 'prevenção'),
        (PROCESS, 'processo'),
        (OTHER, 'outro')
    )
    report = models.ForeignKey(Report, on_delete=models.CASCADE, default='')
    item = models.CharField(max_length=100, default='', verbose_name='Item')
    action_type = models.CharField(max_length=50, choices=ACTION_TYPE_CHOICES, default='other', verbose_name='Type')
    owner = models.CharField(max_length=50, default='', verbose_name='Owner')

    #def __str__(self):
        #return self.item
        #return unicode(self.item, 'utf-8')

    def __unicode__(self):
        return self.item

