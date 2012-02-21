from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'songVotes/', 'song_tracker.songtracker.views.songVotes'),
    url(r'songHearted/', 'song_tracker.songtracker.views.songHearted'),
    url(r'getSongInfo/', 'song_tracker.songtracker.views.getSongInfo'),
    url(r'songPlayed/', 'song_tracker.songtracker.views.songVotes'),
    url(r'catFact/', 'song_tracker.songtracker.views.catFact'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
