from bs4 import BeautifulSoup
from credentials import client_id, client_secret
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scrape billboard top 100 for a user designated date

base_URL = "https://www.billboard.com/charts/hot-100"

target_date = input("What year would you like to travel to? (YYYY-MM-DD): ")

response = requests.get(f"{base_URL}/{target_date}")
web_contents = response.text

soup = BeautifulSoup(web_contents, "html.parser")

song_list = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_list]
print(song_names)

# Authenticate with Spotify

scope = "playlist-modify-private"
client_id = client_id
client_secret = client_secret

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt",
    username="Nick Cramer"
))

user_id = sp.current_user()["id"]

# Search Spotify for the scraped song list

song_uris = []
year = target_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{target_date.upper()} Billboard 100",
    public=False,
    description=f"Billboard 100 for {target_date}"
)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)
