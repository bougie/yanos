from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'priority/([0-9]+)', 'tasks.views.priority', name='tasks_priority'),
    url(r'priority', 'tasks.views.priority', name='tasks_priority'),
    url(r'state/([0-9]+)', 'tasks.views.state', name='tasks_state'),
    url(r'state', 'tasks.views.state', name='tasks_state'),
    url(r'', 'tasks.views.index', name='tasks_index'),
)
