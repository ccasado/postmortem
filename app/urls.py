from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^incidente/(?P<report_id>[0-9]+)/$', views.detail, name='detail'), 
    url(r'^healthcheck.html$', TemplateView.as_view(template_name='healthcheck.html'), name='healthcheck'),
    url(r'^acoes$', views.actions, name='actions'),
    url(r'^numbers$', views.numbers, name='numbers'),
]
