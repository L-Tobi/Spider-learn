from urllib.request import ProxyHandler , build_opener
from test import urllib_test
from test import requests_test
from test import regex_test
from practice import get_movies_rank
from  test import lxml_test

#urllib_test.check_robot_txt('https://www.sina.com.cn')
#requests_test.requests_test()
#regex_test.practice_regex()
#url = 'http://maoyan.com/board/4'
#url = 'http://finance.sina.com.cn/realstock/company/sz002202/nc.shtml'
url = 'https://hq.sinajs.cn/?rn=1534081330022&list=sz002202,sz002202_i'
html = get_movies_rank.get_one_page(url)

#lxml_test.practice_lxml_test(url)
print(html)