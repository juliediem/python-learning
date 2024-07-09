import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
# print(soup.prettify())
#
# test = soup.find_all(class_="article-title-description__text")
# print(test)
# Using List comprehension as a shortcut to for loop
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
print(titles)

reversed_titles = titles[::-1]

with open("top_movies.txt", "w") as movie_file:
    for title in reversed_titles:
        movie_file.write(f"{title}\n")
