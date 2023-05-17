from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
film_list_text = response.text

soup = BeautifulSoup(film_list_text, "html.parser")
film_titles = soup.find_all(name="h3", class_="title")

ranked_film_lst = [film.getText() for film in film_titles]

# for film in film_titles:
#     ranked_film_lst.append(film.getText())

# ranked_film_lst[::-1]
ranked_film_lst.reverse()

with open('Top 100 films.txt', 'w') as f:
    for film in ranked_film_lst:
        f.write(f"{film}\n")


