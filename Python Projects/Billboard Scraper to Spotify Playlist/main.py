from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# user_input_date = str(input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "))
user_input_date = '2020-07-07'
BASE_URL = "https://www.billboard.com/charts/hot-100/"
URL = BASE_URL + user_input_date

response = requests.get(URL)
billboard_100_page = response.text

soup = BeautifulSoup(billboard_100_page, "html.parser")

testSoup=soup.select("li ul li h3")
song_names = [song.getText().strip() for song in testSoup]
print(song_names)

# with open("billboard_100_songs.txt", mode="w") as data:
#     for element in soup.find_all(attrs={'class': 'o-chart-results-list-row-container'}):
#         print(element.h3.get_text(strip=True))
#         data.writelines(f"{element.h3.get_text(strip=True)}\n")


# Authenticate Spotify
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
