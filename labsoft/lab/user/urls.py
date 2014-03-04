from django.conf.urls import patterns, include, url

from labsoft.lab.user.views import(
    create_user,
    UserListView)

urlpatterns = patterns('',
    url(r'^$', UserListView.as_view(), name='labsoft-lab-user-list'),
    url(r'^create/', create_user, name='labsoft-lab-user-create'),
)