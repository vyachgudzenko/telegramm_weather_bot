import requests
from bs4 import BeautifulSoup as BS



def get_html(city):
    url = ("https://sinoptik.ua/погода-" + city)
    response = requests.get(url)
    return response.text

def get_data(html):
    data = []
    soup = BS(html,'lxml')
    min_temperature = soup.find('div',{'class':'min'}).get_text()
    min_temperature = min_temperature.replace('мин.','')
    max_temperature = soup.find('div',{'class':'max'}).get_text()
    max_temperature = max_temperature.replace('макс.','')
    description  = soup.find('div',{'class':'description'}).get_text()
    data.append(min_temperature)
    data.append(max_temperature)
    data.append(description)
    return data
