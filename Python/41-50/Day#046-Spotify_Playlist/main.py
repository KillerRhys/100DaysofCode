""" This Year in Melody
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.02.23-0023 """

# Imports.
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Constants.
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
URL = "https://www.billboard.com/charts/hot-100/"
DATE_TO_REVIST = input("Please enter a date YYYY-MM-DD to build your playlist from: ")

# Use input to fecth song list.
response = requests.get(URL + DATE_TO_REVIST)
data = response.text.encode("ascii", "ignore")

soup = BeautifulSoup(data, "lxml")
song_list = [song.getText().strip() for song in soup.select(".a-no-trucate")[::2]]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = DATE_TO_REVIST.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE_TO_REVIST} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
