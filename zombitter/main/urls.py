from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='home'),
    url(r'^twitt/add/$', 'add_twitt', name='add_twitt'),
    url(r'^twitt/(?P<pk>\d+)$', 'show_twitt', name='show_twitt'),
    url(r'^twitt/(?P<pk>\d+)/edit$', 'edit_twitt', name='edit'),
    url(r'^twitt/(?P<pk>\d+)/delete$', 'delete_twitt', name='delete'),
    url(r'^zombie/add/$', 'add_zombie', name='add_zombie'),
    url(r'^zombie/(?P<pk>\d+)$', 'show_zombie', name='show_zombie'),
    url(r'^zombie/(?P<pk>\d+)/edit$', 'edit_zombie', name='edit'),
    url(r'^zombie/(?P<pk>\d+)/delete$', 'delete_zombie', name='delete'),
)
