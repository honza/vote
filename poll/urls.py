from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'poll.views.index', name='home'),
    url(r'^done/$', 'poll.views.done', name='done'),
    # staff views
    url(r'^staff/$', 'poll.views.staff', name='staff'),
    url(r'^staff/login/$', 'django.contrib.auth.views.login'),
    url(r'^staff/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^staff/voters/$', 'poll.views.voters', name='voters'),
    url(r'^staff/ajax/$', 'poll.views.ajax', name='ajax'),
)
