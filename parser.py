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
    soup = BeautifulSoup(html, 'html.parser') # Для получения html страницы
    items = soup.findAll('div', class_ = 'item product_listbox oh')
    new_list = []#пустой лист ,куда мы будем сохранять наши данные 

    for item in items:
        new_list.append({
            'title': item.find('div', class_ = 'product_text pull-left').find('div', class_ = 'listbox_title oh').find('a').get_text(strip = True),
            'price': item.find('div', class_ = 'motive_box pull-right').find('div', class_ = 'listbox_price text-center').get_text(strip = True),
            'nalichie': item.find('div', class_ = 'motive_box pull-right').find('div', class_ = 'listbox_motive text-center').get_text(strip = True),
            'images': HOST + item.find('div', class_='listbox_img pull-left').find('img').get('src')  #Ссылкм на картинки
        
        })
    return new_list

response = requests.get(URL)
def save(response,path):
    with open(path, 'a') as file:  #Открытие csv файла
        writer = csv.writer(file, delimiter =';')
        writer.writerow(['название',"цена","наличие","фотки"]) # Указываем название столбцов
        for i in response:
            writer.writerow([i['title'],i['price'],i['nalichie'],i['images']]) # Записываем наши данные 

save(get_content(response.text),CSV)
#     for i in re
# print(get_content(response.text))
