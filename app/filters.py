from .models import Report, Action
import django_filters

class ReportFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = ['product', ]

class ActionFilter(django_filters.FilterSet):
    class Meta:
        model = Action
        fields = ['status', ]