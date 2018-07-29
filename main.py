from urllib.error import URLError
from urllib.request import ProxyHandler , build_opener

proxy_handler = ProxyHandler(
    {
        'http' : 'http://127.0.0.1:63231',
        'https' : 'http://127.0.0.1:63231'
    }
)

opener = build_opener(proxy_handler)
try:
    print("***************1")
    response = opener.open('https://www.baidu.com')
    print("***************2")
    print(response.read().decode('utf-8'))
    # headers = {'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X) AppleWebKit / 537.36(KHTML, like Gecko)',
    #            'Host': 'httpbin.org'}
    # dict = {'name':'Tobi'}
    #
    # username= 'username'
    # password= 'password'
    #
    # url = 'http://localhost:5000'
    #
    # p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # p.add_password(None,url,username,password)
    # auth_handler = urllib.request.HTTPBasicAuthHandler(p)
    # opener = urllib.request.build_opener(auth_handler)
    #
    # response = opener.open(url)
    # html = response.read().decode('utf-8')
    # print(html)
    # request = urllib.request.Request('http://httpbin.org/post', headers=headers, data=bytes(urllib.parse.urlencode(dict),encoding='utf8'), method='POST')
    # print("***************")
    # response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
    # if  response.status != 200:
    #     print('status : ' + response.status)
    # print("*******result********")
    # print(response.read().decode('utf-8'))
    # print(type(response))
    # print(response.status)
    # print(response.getheaders())
    # print(response.getheader('Server'))

except URLError as e:
    # if  isinstance(e.reason, socket.timeout):
    #     print('time out!!!')

    print(e.reason)