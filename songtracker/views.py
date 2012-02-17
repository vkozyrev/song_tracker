# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.core import serializers
import datetime, json
from song_tracker.songtracker.models import Song, Room, RoomSongInfo 

SECRET_ID = "auugnsogb92nflac825nwapbps94n2e3"

'''
test example url
http://127.0.0.1:8000/songPlayed?roomName=Coding%20Soundtrack&roomID=4ded3b7e99968e1d29000047&roomURL=http%3A%2F%2Fturntable.fm%2Fcoding_soundtrack3&playedBy=Strngr_Lzr&songArtist=Calvin%20Harris&songName=The%20Rain&secretID=auugnsogb92nflac825nwapbps94n2e3

songtracker.vladimirkozyrev.com/songPlayed?roomName=name&roomID=id&roomURL=url&playedBy=dj&songArtist=artist&songName=song&secretID=key
'''

def songPlayed(request):
    
    roomName = request.GET.get('roomName')
    roomURL = request.GET.get('roomURL')
    playedBy = request.GET.get('playedBy')
    songArtist = request.GET.get('songArtist')
    songName = request.GET.get('songName')
    secretID = request.GET.get('secretID')
    roomID = request.GET.get('roomID')
    
    if request and roomName and roomURL and roomID and playedBy and playedBy and songName and songArtist and secretID and (secretID == SECRET_ID):
        
        try:
            requestRoom = Room.objects.get(room_url = roomURL, room_name = roomName, room_id = roomID)
        except:
            requestRoom = Room(room_url = roomURL, room_name = roomName, room_id = roomID)
            requestRoom.save()
        
        try:    
            requestSong = Song.objects.get(song_name = songName, song_artist = songArtist)
        except:
            requestSong = Song(song_name = songName, song_artist = songArtist)
            requestSong.save()
        
        try:
            roomSongInfo = RoomSongInfo.objects.get(song = requestSong, room = requestRoom)
            numberOfPlays = roomSongInfo.times_played
            lastPlayedBy = roomSongInfo.player_name
            lastPlayedTime = roomSongInfo.time_last_played
            roomSongInfo.times_played = numberOfPlays + 1
            roomSongInfo.player_name = playedBy
            roomSongInfo.save()
            
        except:
            roomSongInfo = RoomSongInfo(room = requestRoom, song = requestSong, player_name = playedBy, time_last_played = datetime.datetime.now(), times_played = 0)
            roomSongInfo.save()
            lastPlayedBy = "First Time Played"
            lastPlayedTime = "0"
            numberOfPlays = 0
        
        returnMap = {"success": True, "timesPlayed": roomSongInfo.times_played, "lastPlayedBy": lastPlayedBy, "lastPlayedTime": str(lastPlayedTime)}
        return HttpResponse(json.dumps(returnMap))
        #return HttpResponse(requestRoom.room_name + " " + requestSong.song_artist + " " + requestSong.song_name + " " + str(roomSongInfo.times_played) + " " + lastPlayedBy + " " + str(lastPlayedTime))
    else:
        
        returnMap = {"success": False}
        return HttpResponse(json.dumps(returnMap))
        #return HttpResponse("ERROR!")