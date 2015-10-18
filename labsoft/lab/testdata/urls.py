from django.conf.urls import patterns, include, url
from labsoft.lab.testdata.views import(
    TestDataListView,
    TestDataCreateView,
    TestDataUpdateView,
    TestDataDetailView)

urlpatterns = patterns('',
    url(r'^$', TestDataListView.as_view(), name='labsoft-lab-testdata-list'),
    url(r'^create/', TestDataCreateView.as_view(), name='labsoft-lab-testdata-create'),
    url(r'^(?P<pk>\d+)/update/$', TestDataUpdateView.as_view(), name='labsoft-lab-testdata-update'),
    url(r'^(?P<pk>\d+)/$', TestDataDetailView.as_view(), name='labsoft-lab-testdata-detail'),
)
