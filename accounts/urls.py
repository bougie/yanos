from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'login', 'accounts.views.login', name='accounts_login'),
    url(r'logout', 'accounts.views.logout', name='accounts_logout'),
    url(r'register', 'accounts.views.register', name='accounts_register'),
    url(r'password', 'accounts.views.password', name='accounts_password'),
    url(r'^$', 'accounts.views.index', name='accounts_index'),
)
