from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="lab/index.html"), name='labsoft-lab-index'),
    url(r'^clients/', include('labsoft.lab.client.urls')),
    #url(r'^materials/', include('mysite.web.material.urls')),
    
)
