from django.conf.urls import patterns, include, url
from labsoft.lab.equipment.views import(
    EquipmentListView,
    EquipmentCreateView,
    EquipmentUpdateView,
    EquipmentDetailView,
    EquipmentSampleCreateView,
    EquipmentSampleListView)

urlpatterns = patterns('',
    url(r'^$', EquipmentListView.as_view(), name='labsoft-lab-equipment-list'),
    url(r'^create/', EquipmentCreateView.as_view(), name='labsoft-lab-equipment-create'),
    url(r'^(?P<pk>\d+)/update/$', EquipmentUpdateView.as_view(), name='labsoft-lab-equipment-update'),
    url(r'^(?P<pk>\d+)/samples/$', EquipmentSampleListView.as_view(), name='labsoft-lab-equipment-sample-list'),
    url(r'^(?P<pk>\d+)/samples/create/$', EquipmentSampleCreateView.as_view(), name='labsoft-lab-equipment-sample-create'),
    url(r'^(?P<pk>\d+)/$', EquipmentDetailView.as_view(), name='labsoft-lab-equipment-detail'),
)
