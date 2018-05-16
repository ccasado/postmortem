# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Report, Action, Product, Author, System

admin.site.register(Report)
admin.site.register(Action)
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(System)

