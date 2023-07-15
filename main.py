import requests
from bs4 import BeautifulSoup

URL = "http://novey.uz/uz/site/catalog?type=all" # Replace this with the website's URL
getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})

soup = BeautifulSoup(getURL.text, 'html.parser')

all_models = soup.findAll('div', class_='product')

for model in all_models:
    print(model.text)




# links = []
# for link in all_models.findAll('a'):
#     links.append(link.get('href'))


# print(all_models)
# images = soup.find_all('img')
# print(images)