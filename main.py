from urllib.request import ProxyHandler , build_opener
from test import urllib_test
from test import requests_test
from test import regex_test
from stock import get_stock_info
#from test import beautifulsoup_test
from  test import lxml_test
import sys
import re
import time
from time import sleep
#urllib_test.check_robot_txt('https://www.sina.com.cn')
#requests_test.requests_test()
#regex_test.practice_regex()
#url = 'http://finance.sina.com.cn/realstock/company/sz002202/nc.shtml'


#while(True):
    # try:
       # url = 'https://hq.sinajs.cn/?rn=1534081330022&list=sz002202,sz002202_i'
       # url = 'http://finance.sina.com.cn/realstock/company/sz002202/nc.shtml'
       # get_stock_info.get_stock_start(url)
get_stock_info.get_valid_stock_code('60')
    #    sleep(5)
    # except:
    #     print('something is wrong')
    #     sleep(10)

#lxml_test.practice_lxml_test(url)

#beautifulsoup_test.practice_beautifulsoup()\


