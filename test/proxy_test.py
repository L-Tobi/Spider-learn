from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
import requests


def addProxy():
    proxy = '127.0.0.1:63231'
    proxy_handler = ProxyHandler(
        {
            'http': 'socks5://' + proxy,
            'https': 'socks5://' + proxy
        }
    )

    #opener = build_opener(proxy_handler)
    try:
        #response = opener.open('http://httpbin.org/get')
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print (response.text)
        #print (response.read().decode('utf-8'))
    except URLError as e:
        print (e.reason)