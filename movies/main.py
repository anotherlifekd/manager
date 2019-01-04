import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep

ROOT_URL = 'https://ua.kinorium.com/movies/cinema/'
MOVIES_URL = 'https://ua.kinorium.com'
MOVIES_LIST_URL = []

def random_sleep():
    sleep(random.randint(1, 3))

useragent = UserAgent()

with open('./cinema.txt', 'w') as file:
    headers = {
        'User-Agent': useragent.random,
    }
    response = requests.get(ROOT_URL, headers=headers)
    random_sleep()
    assert response.status_code == 200
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    movies_list = soup.findAll('div', {'class': 'filmList__item-title-wrap'})
    for movie in movies_list:
        a = movie.find_all('a', href=True)[0]
        href = a['href']
        MOVIES_LIST_URL.append(href)

    for film_url in MOVIES_LIST_URL:
        film = requests.get(MOVIES_URL + film_url, headers=headers)
        random_sleep()
        html_doc_film = film.text
        soup_film = BeautifulSoup(html_doc_film, 'html.parser')

        #get movie name
        name = soup_film.find('span', {'class': 'film-page__itemprop'})
        film_name = name.text

        #get movie year
        full_info = soup_film.find_all('td')[1]
        film_year = full_info.find('a').text

        #get duration
        duration = soup_film.find_all('td')[5].text

        #get movie country
        country = soup_film.find_all('td')[3].find_all('a')
        country_list = []
        for i in country:
            country_list.append(i.text)

        #rank IMDb
        rank = soup_film.find('ul', {'class': 'ratingsBlock'})
        imdb = rank.findAll('span')[6].text

        #Genre
        genre = soup_film.find_all('a', itemprop='genre')
        genre_list = []
        for name_genre in genre:
            genre_list.append(name_genre.text)

        #Budget
        film_budget = ''
        rows = soup_film.find_all('tr')
        for row in rows:
            cols = row.find_all('td', {'class': 'data'})
            for col in cols:
                budget = str(col.text)
                if budget.startswith(' $'):
                    film_budget = budget

        #Description
        description = soup_film.find('div', {'class': 'film-page__text'}).text

        file.write(f'Назва фільму: {film_name}\nрік: {film_year}\nкраїна: {country_list}\n'
                   f'тривалість: {duration}\nбюджет: {film_budget}\nIMDb: {imdb}\nжанр: {genre_list}\n'
                   f'опис: {description}\nurl: https://ua.kinorium.com{film_url}\n\n\n')