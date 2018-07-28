import urllib.request
import urllib.parse
import ssl
import urllib.error
import socket
try:
    headers = {'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X) AppleWebKit / 537.36(KHTML, like Gecko)',
               'Host': 'httpbin.org'}
    dict = {'name':'Tobi'}
    request = urllib.request.Request('http://httpbin.org/post', headers=headers, data=bytes(urllib.parse.urlencode(dict),encoding='utf8'), method='POST')
    print("***************")
    response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
    if  response.status != 200:
        print('status : ' + response.status)
    print("*******result********")
    print(response.read().decode('utf-8'))
    print(type(response))
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))

except urllib.error.URLError as e:
    if  isinstance(e.reason, socket.timeout):
        print('time out!!!')

    print('error ' + e.reason)