from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /report/
    url(r'^$', views.index, name='index'),
    # ex: /report/2/
    url(r'^(?P<report_id>[0-9]+)/$', views.detail, name='detail'), 
]