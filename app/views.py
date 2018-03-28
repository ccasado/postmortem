# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from .models import Report
from .filters import ReportFilter

@cache_page(60 * 1)
def index(request):
    report_list = Report.objects.order_by('-pub_date')
    report_filter = ReportFilter(request.GET, queryset=report_list)
    return render(request, 'reports/index.html', {'filter': report_filter})

@cache_page(60 * 1)
def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'reports/detail.html', {'report':report})
