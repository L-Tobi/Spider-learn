from urllib.request import ProxyHandler , build_opener
from test import urllib_test
from test import requests_test
from test import regex_test
from stock import get_stock_info
from  test import lxml_test
import sys
import re
import time
from time import sleep
from test import proxy_test
from database import operation

#urllib_test.check_robot_txt('https://www.sina.com.cn')
#requests_test.requests_test()
#regex_test.practice_regex()
#url = 'http://finance.sina.com.cn/realstock/company/sz002202/nc.shtml'


#try:
# get_stock_info.get_stock_codes_info()
#operation.create_database("STOCK_INFO")
#operation.create_table('test')
get_stock_info.get_stock_code_basis_info()
    #get_stock_info.get_valid_stock_code('60')
#except:
 #   print('something is wrong')
 #   sleep(10)

#lxml_test.practice_lxml_test(url)

#beautifulsoup_test.practice_beautifulsoup()\


