from django.conf.urls.defaults import patterns, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='home'),
    url(r'^(?P<zombie_name>\w+)/?$', 'zombie_tweets', name='zombie_tweets'),
    url(r'^tweet/(?P<id_tweet>\d+)/?$', 'tweet', name='tweet'),
    url(r'^crud/zombies/?$', 'crud', name='crud'),
    url(r'^crud/zombies/delete/(?P<zombie_id>\d+)/?$', 'delete_zombie', name='delete_zombie'),
    url(r'^crud/zombies/edit/(?P<zombie_id>\d+)/?$', 'edit_zombie', name='edit_zombie'),
    url(r'^crud/zombies/add/?$', 'add_new', name='add_new'),
)
