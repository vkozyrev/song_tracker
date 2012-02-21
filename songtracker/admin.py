from song_tracker.songtracker.models import Song, Room, RoomSongInfo, CatFact
from django.contrib import admin

admin.site.register(Song)
admin.site.register(Room)
admin.site.register(RoomSongInfo)
admin.site.register(CatFact)