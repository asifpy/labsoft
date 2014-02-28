from django.conf.urls import patterns, include, url
from labsoft.lab.client.views import(
    ClientCompanyListView,
    ClientCompanyCreateView,
    ClientCompanyUpdateView,
    ClientCompanyDetailView)

urlpatterns = patterns('',
    url(r'^$', ClientCompanyListView.as_view(), name='labsoft-lab-client-list'),
    url(r'^create/', ClientCompanyCreateView.as_view(), name='labsoft-lab-client-create'),
    url(r'^(?P<pk>\d+)/update/$', ClientCompanyUpdateView.as_view(), name='labsoft-lab-client-update'),
    url(r'^(?P<pk>\d+)/$', ClientCompanyDetailView.as_view(), name='labsoft-lab-client-detail'),
)
