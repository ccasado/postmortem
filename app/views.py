# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from django.db.models import Count
from .models import Report, Action
from .filters import ReportFilter, ActionFilter
from django.db.models import Q



@cache_page(60 * 1)
def index(request):
    report_list = Report.objects.order_by('-date')
    report_filter = ReportFilter(request.GET, queryset=report_list)
    reports_action_pending = Report.objects.filter(Q(action__status='TODO'))

    rlist = []
    for report_action in reports_action_pending:
        rlist.append(report_action.pk)

    return render(request, 'reports/index.html', {'filter': report_filter, 'actions_pending': rlist})


@cache_page(60 * 1)
def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'reports/detail.html', {'report': report})


def actions(request):
    action_list = Action.objects.order_by('-pub_date')
    action_filter = ActionFilter(request.GET, queryset=action_list)
    return render(request, 'reports/actions.html', {'filter': action_filter})


def numbers(request):
    report = Report.objects.values('product').annotate(total=Count('product')).order_by()
    return render(request, 'reports/numbers.html', {'report': report})
