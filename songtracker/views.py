# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.core import serializers
import datetime
from song_tracker.songtracker.models import Song, Room, RoomSongInfo 

SECRET_ID = "auugnsogb92nflac825nwapbps94n2e3"

'''
http://127.0.0.1:8000/songPlayed?roomName=Coding%20Soundtrack&roomURL=http%3A%2F%2Fturntable.fm%2Fcoding_soundtrack3&playedBy=Strngr_Lzr&songArtist=Calvin%20Harris&songName=The%20Rain&secretID=auugnsogb92nflac825nwapbps94n2e3
'''

def songPlayed(request):
    
    roomName = request.GET.get('roomName')
    roomURL = request.GET.get('roomURL')
    playedBy = request.GET.get('playedBy')
    songArtist = request.GET.get('songArtist')
    songName = request.GET.get('songName')
    secretID = request.GET.get('secretID')
    
    if request and roomName and roomURL and playedBy and playedBy and songName and songArtist and secretID and (secretID == SECRET_ID):
        
        newRoom = False
        newSong = False
        newConnection = False
        try:
            requestRoom = Room.objects.get(room_url = roomURL, room_name = roomName)
            print requestRoom
        except Exception as inst:
            print inst
            print("New Room")
            requestRoom = Room(room_url = roomURL, room_name = roomName)
            requestRoom.save()
            newRoom = True
        
        try:    
            requestSong = Song.objects.get(song_name = songName, song_artist = songArtist)
            print requestSong
        except Exception as inst:
            print inst
            print("New Song")
            requestSong = Song(song_name = songName, song_artist = songArtist)
            requestSong.save()
            newSong = True
        
        try:
            print "HELLO!"
            roomSongInfo = RoomSongInfo.objects.get(song = requestSong, room = requestRoom)
            numberOfPlays = roomSongInfo.times_played
            lastPlayedBy = roomSongInfo.player_name
            lastPlayedTime = roomSongInfo.time_last_played
            roomSongInfo.times_played = numberOfPlays + 1
            roomSongInfo.player_name = playedBy
            roomSongInfo.save()
            print "BYE!"
            
        except Exception as inst:
            print inst
            roomSongInfo = RoomSongInfo(room = requestRoom, song = requestSong, player_name = playedBy, time_last_played = datetime.datetime.now(), times_played = 0)
            roomSongInfo.save()
            lastPlayedBy = "First Time Played"
            lastPlayedTime = "0"
            numberOfPlays = 0
            newConnection = True;
        
        return HttpResponse(requestRoom.room_name + " " + requestSong.song_artist + " " + requestSong.song_name + " " + str(roomSongInfo.times_played))
    else:
        
        return HttpResponse("ERROR!")