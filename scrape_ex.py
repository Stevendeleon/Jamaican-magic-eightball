import requests
from bs4 import BeautifulSoup
import pandas as pd

items = []

for x in range(1,113):
    url = "https://newworldfans.com/db?page="
    r = requests.get(url+str(x))
    soup = BeautifulSoup(r.content, 'html.parser')
    t_body = soup.find('div', {"class": "table-wrapper"}).find('table').find('tbody')

    for tr in t_body.find_all('tr'):
        try:
            img = tr.find('img', {"src": True})['src']
        except:
            img = "not_found"
        name = tr.find_all('td')[1].text.strip()
        slot = tr.find_all('td')[2].text.strip()[7:]
        item_type = tr.find_all('td')[3].text.strip()[7:]
        tier = tr.find_all('td')[4].text.strip()[7:]
        gear_score = tr.find_all('td')[5].text.strip()[13:]
        level = tr.find_all('td')[6].text.strip()[8:]
        bop = tr.find_all('td')[7].text.strip()[17:]
        craft = tr.find_all('td')[8].text.strip()[13:]

        item_details = {
            "img": img,
            "name": name,
            "slot": slot,
            "type": item_type,
            "tier": tier,
            "gear_score": gear_score,
            "level": level,
            "bind_on_pickup": bop,
            "crafted_by": craft
        }
        items.append(item_details)
    print('Total items Scanned: ', len(items))
    print('current page: ', (url+str(x))[33:])

df = pd.DataFrame(items)
df.to_csv('item-names.csv')