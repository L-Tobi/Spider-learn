import requests
from requests import Request, Session
def requests_test():
#     data = {'name' : 'tobi', 'age' : '27'}
#     r = requests.post('https://httpbin.org/post',data=data)
#     print(r.text)
#
#     r2 = requests.get('https://github.com/favicon.ico')
#     print(r2.text)
#     print(r2.content)
#
# #   store ico to disk.
#     with open('favicon.ico', 'wb') as f:
#         f.write(r2.content)
#
#
        # s = requests.session()
        # s.get('http://httpbin.org/cookies/set/number/123456')
        # r = s.get('http://httpbin.org/cookies')
        # print(r.text)
        #
        # response = requests.get('http://www.12306.cn/cookies')
        # print(response.status_code)

    # proxies = {
    #     'http' : '127.0.0.1:62231'
    # }
    url = 'http://httpbin.org/post'
    data = {
        'name' : 'tobi'
    }
    head = {

    }
    s = Session()
    req = Request('POST',url,data=data, headers=head)
    prepped = s.prepare_request(req)
    r = s.send(prepped)
    print(r.text)