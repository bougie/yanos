from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^accounts/', include('accounts.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^$', include('core.urls')),
)
