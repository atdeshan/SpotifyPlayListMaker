import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
date = input("Enter the date that you want to create a playlist")
songList=[]
songId = []
clientId = "f399481d991e43bc8c0c8e416896c9bf"
clientSecret = "c34f038e78294c8c9fccb7ed9401dc1d"
redirectURL = "http://example.com"
scope = "playlist-modify-public"

auth = SpotifyOAuth(client_id=clientId,client_secret=clientSecret,redirect_uri=redirectURL,scope=scope)
sp = spotipy.Spotify(auth_manager= auth)

def getSongList():
    global songList
    web = requests.get("https://www.billboard.com/charts/hot-100/2024-07-06/")
    soup = bs4.BeautifulSoup(web.text,"html.parser")
    names = soup.select("li ul li h3")
    songList = [i.getText().strip() for i in names]

def getSongId(songs):
    global songId
    
    for i in songs:
        songId.append(sp.search(q=i,limit=1,type="track")["tracks"]["items"][0]["id"])


getSongList()
getSongId(songList)

userId = sp.current_user()['id']
playlistName = "this is "
palylistDis = "sdf"
playList = sp.user_playlist_create(user=userId,name=playlistName,public=True,description=palylistDis)
playlistId = playList['id']
sp.playlist_add_items(playlist_id=playlistId,items=songId)

