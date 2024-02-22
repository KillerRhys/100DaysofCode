""" Movies to Watch
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.02.21-2100"""

# Imports.
from bs4 import BeautifulSoup
import requests

# URL to grab data from.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch Data from website and make BS4 object.
response = requests.get(URL)
website_data = response.text.encode('ascii', 'ignore')
soup = BeautifulSoup(website_data, "html.parser")

# Fetch movie titles / numbers, reverse list and print to file.
movies = soup.find_all("h3")
movie_list = [movie.getText() for movie in movies]
movie_list.reverse()
with open("movies.txt", "w+") as file:
    for item in movie_list:
        file.writelines(item + "\n")

file.close()
