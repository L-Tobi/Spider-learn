from urllib.request import ProxyHandler , build_opener
from test import urllib_test
from test import requests_test
from test import regex_test
from practice import get_movies_rank
from test import beautifulsoup_test
from  test import lxml_test
import sys
import re
from time import sleep
#urllib_test.check_robot_txt('https://www.sina.com.cn')
#requests_test.requests_test()
#regex_test.practice_regex()
#url = 'http://maoyan.com/board/4'
#url = 'http://finance.sina.com.cn/realstock/company/sz002202/nc.shtml'
while(True):
    url = 'https://hq.sinajs.cn/?rn=1534081330022&list=sz002202,sz002202_i'
    html = get_movies_rank.get_one_page(url)
    #print(html)

    #price = re.match('^var.*,\d.*|', html)
    price = re.search(',.*?,.*?,.*?,.*?,.*?,.*?,.*?,' ,html,re.S)
    result = price.group(0)
    #print(result)
    result =  result.split(',')

    print('open :', result[1],end='', flush = True)
    print('yesterday :', result[2],end='', flush = True)
    print('current :', result[3],end='', flush = True)
    print('highest :', result[4],end='', flush = True)
    print('lowest :', result[5],end='', flush = True)
    sys.stdout.flush()
    sleep(5)
#lxml_test.practice_lxml_test(url)

#beautifulsoup_test.practice_beautifulsoup()