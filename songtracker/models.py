from django.db import models

class Song(models.Model):
    song_name = models.CharField(verbose_name = 'Song Name', max_length = 100)
    song_artist = models.CharField(verbose_name = 'Song Artist', max_length = 100)
    room = models.ManyToManyField("Room", through="RoomSongInfo", verbose_name = "Room")
    
    def __unicode__(self):
        return self.song_name
    
class Room(models.Model):
    room_url = models.URLField(verbose_name = 'Room URL', max_length = 200)
    room_name = models.CharField(verbose_name = 'Room Name', max_length = 100)
    
    def __unicode__(self):
        return self.room_name
    
class RoomSongInfo(models.Model):
    player_name = models.CharField(verbose_name = 'Name of who played the song last', max_length = 100)
    time_last_played = models.TimeField(verbose_name = 'Time Played')
    times_played = models.IntegerField(verbose_name = 'Times Played')
    song = models.ForeignKey("Song", verbose_name = "Song")
    room = models.ForeignKey("Room", verbose_name = 'Room Played In')
    
    def __unicode__(self):
        return self.player_name
    