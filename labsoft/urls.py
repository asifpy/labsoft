from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import autocomplete_light.shortcuts as al
from django.contrib import admin

# import every app/autocomplete_light_registry.py
al.autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'labsoft.core.views.index', name='labsoft-index'),
	url(r'^index/$', TemplateView.as_view(template_name="login_success.html"), name='labsoft-index'),
    url(r'^lab/', include('labsoft.lab.urls')),
    
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
