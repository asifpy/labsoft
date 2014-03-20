from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="lab/index.html"), name='labsoft-lab-index'),
    url(r'^clients/', include('labsoft.lab.client.urls')),
    url(r'^users/', include('labsoft.lab.user.urls')),
    url(r'^equipments/', include('labsoft.lab.equipment.urls')),
    url(r'^samples/', include('labsoft.lab.sample.urls')),
)
