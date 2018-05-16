# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from .slack import slack
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ('name',)

class System(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ('name',)

class Author(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.email)

    class Meta:
        ordering = ('name',)

class Report(models.Model):
    date = models.DateField('Date')
    pub_date = models.DateTimeField('Date published', auto_now=True)
    start_time = models.TimeField('Start Time', null=True, blank=True, help_text='Momento em que o incidente tem início.')
    end_time = models.TimeField('End Time', null=True, blank=True, help_text='Momento em que o incidente é controlado.')
    detect_time = models.TimeField('Detect Time', null=True, blank=True, help_text='Momento em que o incidente é percebido, seja por pessoas ou sistemas.')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produto', help_text='Produto impactado pelo incidente.')
    authors = models.ManyToManyField(Author)
    systems = models.ManyToManyField(System)
    systems.help_text = 'Sistemas envolvidos no incidente.'
    summary = models.CharField(max_length=100, default='', verbose_name='Summary')
    impact = models.TextField('Impact', default='', help_text='Efeito sobre o usuário final ou ao negócio.')
    root_causes = models.TextField('Root causes', default='', help_text='Explicação sobre as circunstâncias em que o incidente ocorreu. Pode ser útil usar a técnica 5 Whys.')
    trigger = models.CharField(max_length=100, default='', verbose_name='Trigger', blank=True)
    resolution = models.TextField('Resolution', default='', help_text='Explicação sobre as ações para controlar o incidente.')
    detection = models.CharField(max_length=100, default='', verbose_name='Detection', blank=True)

    def __str__(self):
        return self.summary

    def save(self, *args, **kwargs):
        if self.pk is None:
            created = True
        else:
            created = False
        super(Report, self).save(*args, **kwargs)
        report_id = int(self.pk)
        if settings.SLACK_ENABLE and created:
            slack("Novo postmortem criado: %s em %s. Acesse aqui %s/incidente/%d/" % (self.summary, self.date, settings.HOST, report_id))

class Action(models.Model):
    MITIGATE = 'Mitigação'
    PREVENT = 'Prevenção'
    PROCESS = 'Processo'
    OTHER = 'Outro'
    ACTION_TYPE_CHOICES = (
        (MITIGATE, 'mitigação'),
        (PREVENT, 'prevenção'),
        (PROCESS, 'processo'),
        (OTHER, 'outro')
    )
    TODO = 'TODO'
    DONE = 'Concluído'
    STATUS = (
        (TODO, 'TODO'),
        (DONE, 'Concluído'),
    )
    report = models.ForeignKey(Report, on_delete=models.CASCADE, default='')
    item = models.CharField(max_length=100, default='', verbose_name='Item')
    pub_date = models.DateTimeField('Date published', auto_now=True)
    action_type = models.CharField(max_length=50, choices=ACTION_TYPE_CHOICES, default='other', verbose_name='Type')
    owner = models.CharField(max_length=50, default='', verbose_name='Owner')
    status = models.CharField(max_length=50, choices=STATUS, default='TODO', verbose_name='Status')

    def __unicode__(self):
        return self.item
