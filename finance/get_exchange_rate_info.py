import requests
from bs4 import BeautifulSoup

current_exchange_rate = 5
current_exchange_rate_date = 6
current_exchange_rate_seconds = 7


def get_exchange_rate():
    url = 'http://www.boc.cn/sourcedb/whpj/'
    result = requests.get(url)

    soup = BeautifulSoup(result.text, 'lxml')
    print('===========')
    # print (soup.div.children)
    # print (soup.select('tr'))
    for i,th in enumerate( soup.div.find_all(name='tr')):
        if i > 1 and i < 29:
            try:
                print (th.find_all(name='td')[current_exchange_rate])
                print (th.find_all(name='td')[current_exchange_rate_date])
                print (th.find_all(name='td')[current_exchange_rate_seconds])
                print (i)
            except Exception as e:
                print (str(e), i)
        print ('=============================')
    # print (soup.find_all(attrs={'class':'odd'}))
    # for ul in soup.find_all(name='tr'):
    #     print(ul.find_all(name='td'))



