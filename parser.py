import requests
from bs4 import BeautifulSoup

import csv

CSV = 'kivano_nout.csv' 
HOST = 'https://www.kivano.kg'
URL = 'https://www.kivano.kg/noutbuki'
HEADERS = {
   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
}

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_ = 'item product_listbox oh')
    new_list = []

    for item in items:
        new_list.append({
            'title': item.find('div', class_ = 'product_text pull-left').find('div', class_ = 'listbox_title oh').find('a').get_text(strip = True),
            'price': item.find('div', class_ = 'motive_box pull-right').find('div', class_ = 'listbox_price text-center').get_text(strip = True),
            'nalichie': item.find('div', class_ = 'motive_box pull-right').find('div', class_ = 'listbox_motive text-center').get_text(strip = True),
            'images': HOST + item.find('div', class_='listbox_img pull-left').find('img').get('src')
        
        })
    return new_list

response = requests.get(URL)
def save(response,path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter =';')
        writer.writerow(['название',"цена","наличие","фотки"])
        for i in response:
            writer.writerow([i['title'],i['price'],i['nalichie'],i['images']])

save(get_content(response.text),CSV)
