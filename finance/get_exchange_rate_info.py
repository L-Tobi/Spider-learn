import requests
from bs4 import BeautifulSoup

def get_exchange_rate():
    url = 'http://www.boc.cn/sourcedb/whpj/'
    result = requests.get(url)

    soup = BeautifulSoup(result.text, 'lxml')
    print('===========')
    for ul in soup.find_all(name='tr'):
        print(ul.find_all(name='td'))



