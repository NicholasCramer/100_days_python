import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.encoding = "utf-8"
web_contents = response.text

soup = BeautifulSoup(web_contents, "html.parser")

movies = []
movie_list = soup.find_all(name="h3", class_="title")
for movie in movie_list:
    title = movie.getText()
    movies.append(title)

movies.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for item in movies:
        file.write(f"{item}\n")
