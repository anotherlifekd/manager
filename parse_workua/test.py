from pdb import set_trace
from time import sleep
import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ROOT_URL = 'https://www.work.ua/ru/jobs/'


def random_sleep():
    sleep(random.randint(1, 3))

useragent = UserAgent()
page = 0
ids = set()
hrefs_list = []

with open('./workua.txt', 'w') as the_file:
    while page != 1:
        page += 1
        headers = {
            'User-Agent': useragent.random,
        }
        print('Page: ', page)
        response = requests.get(ROOT_URL, params={'page': page}, headers=headers)
        random_sleep()
        assert response.status_code == 200
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        job_list = soup.find('div', {'id': 'pjax-job-list'})

        if job_list is None:
            break

        cards = job_list.findAll('div', {'class': 'card-hover'})
        for card in cards:
            a = card.find_all('a', href=True)[0]
            href = a['href']
            id_ = href.split('/')[-2]
            title = a['title']
            if id_ not in ids:
                #the_file.write(f'id:{id_};href:{href};title:{title}\n')
                ids.add(id_)
            #hrefs_list.append(id_)
            resp = requests.get(ROOT_URL + id_, headers=headers)
            html_doc_card = resp.text
            soup_card = BeautifulSoup(html_doc_card, 'html.parser')

            # get company name

            something_1 = soup_card.find('dl', {'class': 'dl-horizontal'})
            company = something_1.find('a')
            title_company = company['title']
            print(company)
            print(title_company)
            #something_2 = something_1.get("dd")
            city = something_1.findAll('dd')[1]
            print(city.text)
            set_trace()

            #film_name = name.text






#        for card_id in hrefs_list:
#            resp = requests.get(ROOT_URL + card_id, headers=headers)
#            #random_sleep()
#            html_doc_card = resp.text
#            soup_card = BeautifulSoup(html_doc_card, 'html.parser')


set_trace()