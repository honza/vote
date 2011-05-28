from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'poll.views.index', name='home'),
    url(r'^done/$', 'poll.views.done', name='done'),
)
