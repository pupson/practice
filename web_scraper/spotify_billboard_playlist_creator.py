import requests
import spotipy
from datetime import datetime

from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


spotify_client_id = CLIENT_ID
spotify_client_secret = CLIENT_SECRET
spotify_redirect_url = "http://example.com"
spotify_scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret,
                redirect_uri=spotify_redirect_url, scope=spotify_scope, show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]
user_date = input("What date would you like the top 100 songs from? (YYYY-MM-DD): ")
bb_url = f"https://www.billboard.com/charts/hot-100/{user_date}"
dt = datetime.strptime(user_date, '%Y-%m-%d')
year = dt.year

response = requests.get(bb_url)

bb_text = response.text

soup = BeautifulSoup(bb_text, "html.parser")
soup_titles = soup.select("li ul li h3")
song_title = [song.get_text().strip() for song in soup_titles]
top_5 = song_title[:5]

song_uris = []
for title in top_5:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
