import requests
from bs4 import BeautifulSoup
from typing import List

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


all_movies: List[str] = soup.find_all(name='h3', class_='title')
all_movies = [movie.getText() for movie in all_movies[::-1]]

with open('movies.txt', 'w') as file:
    for movie in all_movies:
        file.write(f'{movie}\n')
