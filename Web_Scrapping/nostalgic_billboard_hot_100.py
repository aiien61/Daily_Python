import spotipy
import requests
from typing import List
from pprint import pprint
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

billboard_url: str = "https://www.billboard.com/charts/hot-100/"
song_names: List[str] = ['The list of song', 'title from your', 'web scrape']

date: str = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
response = requests.get(billboard_url + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names: List[str] = [song.getText().strip() for song in soup.select('li ul li h3')]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id='YOUR UNIQUE CLIENT ID',
        client_secret='YOUR UNIQUE CLIENT SECRET',
        show_dialog=True,
        cache_path='token.txt',
        username='YOUR SPOTIFY DISPLAY NAME'
    )
)

user_id = sp.current_user()["id"]
print(user_id)


song_uris: List[str] = []
year: str = date.split('-')[0]

for song in song_names:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    pprint(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=True)
pprint(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
