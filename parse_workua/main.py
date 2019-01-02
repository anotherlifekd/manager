from pdb import set_trace

import requests
from bs4 import BeautifulSoup
ROOT_URL = 'https://www.work.ua/ru/jobs/'

result_dict = {}
page = 0

with open('./base-workua.txt', 'w') as file:
    while page != 4:
        page += 1
        response = requests.get(ROOT_URL, params={'page': page})
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
            file.write(f'id:{id_};href:{href};title:{title}\n')
set_trace()