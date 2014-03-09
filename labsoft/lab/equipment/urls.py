from django.conf.urls import patterns, include, url
from labsoft.lab.equipment.views import(
    EquipmentListView,
    EquipmentCreateView,
    EquipmentUpdateView,
    EquipmentDetailView)

urlpatterns = patterns('',
    url(r'^$', EquipmentListView.as_view(), name='labsoft-lab-equipment-list'),
    url(r'^create/', EquipmentCreateView.as_view(), name='labsoft-lab-equipment-create'),
    url(r'^(?P<pk>\d+)/update/$', EquipmentUpdateView.as_view(), name='labsoft-lab-equipment-update'),
    url(r'^(?P<pk>\d+)/$', EquipmentDetailView.as_view(), name='labsoft-lab-equipment-detail'),
)
