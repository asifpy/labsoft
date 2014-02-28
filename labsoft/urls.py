from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'labsoft.core.views.index', name='labsoft-index'),
    url(r'^index/$', TemplateView.as_view(template_name="login_success.html"), name='labsoft-index'),
    url(r'^lab/', include('labsoft.lab.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
