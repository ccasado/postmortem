# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Report, Action, Meeting


admin.site.register(Report)
admin.site.register(Action)


