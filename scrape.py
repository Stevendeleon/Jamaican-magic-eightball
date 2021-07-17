import requests
from bs4 import BeautifulSoup

responses = []
wod = ""

url = "https://jamaicanpatwah.com"
def word_of_day():
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.find('div', {
        "class": "wft-day"
    }).find("h2").text.strip())


