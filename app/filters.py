from .models import Report
import django_filters

class ReportFilter(django_filters.FilterSet):
    class Meta:
        model = Report
        fields = ['product', ]