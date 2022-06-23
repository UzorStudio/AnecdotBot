import requests
from bs4 import BeautifulSoup

def getAnekdot():
    url = "https://nekdo.ru/random/"
    anecdot = {}


    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.text, 'lxml')
    anecdot["anekdot"] = soup.find('div', class_="text").text
    print(anecdot)
    return anecdot


