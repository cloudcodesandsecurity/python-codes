from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


date = input("Which Year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(f"{URL}{date}")
website_html = response.text


soup = BeautifulSoup(website_html, 'html.parser')
music_title = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_names = [song.getText().strip("\n\t") for song in music_title]


print(song_names)
# To reverse the order
songs = song_names[::-1]
print(songs)

# The code below creates the file movies.txt from website
with open("song_names.txt", mode="w") as file:
    for song in songs:
        file.write(f"{song}\n")

# https://developer.spotify.com/
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id=your client id,
        client_secret=your secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)