from django.conf.urls import patterns, include, url
from labsoft.lab.testdata.views import(
    EquipmentSampleListView,
    EquipmentSampleCreateView,
    EquipmentSampleUpdateView,
    EquipmentSampleDetailView)

urlpatterns = patterns('',
    url(r'^$', EquipmentSampleListView.as_view(), name='labsoft-lab-sample-list'),
    url(r'^create/', EquipmentSampleCreateView.as_view(), name='labsoft-lab-sample-create'),
    url(r'^(?P<pk>\d+)/update/$', EquipmentSampleUpdateView.as_view(), name='labsoft-lab-sample-update'),
    url(r'^(?P<pk>\d+)/$', EquipmentSampleDetailView.as_view(), name='labsoft-lab-sample-detail'),
)
