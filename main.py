from urllib.request import ProxyHandler , build_opener
from test import urllib_test
from test import requests_test
from test import regex_test
from finance import get_stock_info
from finance import get_exchange_rate_info
from  test import lxml_test
import sys
import re
import time
import threading
from smtp import mail
from datetime import datetime
from time import sleep
from test import proxy_test
from database import operation

#urllib_test.check_robot_txt('https://www.sina.com.cn')

pm_start_time = time.strftime("%Y-%m-%d ", time.localtime()) + '13:00:00'
pm_end_time = time.strftime("%Y-%m-%d ", time.localtime()) + '15:01:00'
am_start_time = time.strftime("%Y-%m-%d ", time.localtime()) + '09:25:00'
am_end_time = time.strftime("%Y-%m-%d ", time.localtime()) + '11:31:00'

collect_summary_data = True
#try:
# get_stock_info.get_stock_code_basis_info(True)

exchange_rate_time = datetime.now()

def get_realtime_stock_info():
    while(True):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if (current_time > am_start_time and current_time < am_end_time) or (current_time > pm_start_time and current_time < pm_end_time):
            get_stock_info.get_stock_codes_info(current_time)
        sleep(10000)

thread_realtime = threading.Thread(target=get_realtime_stock_info)
thread_realtime.start()


while(True):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if ((datetime.now() - exchange_rate_time).seconds > 300):
        get_exchange_rate_info.get_exchange_rate()
        exchange_rate_time = datetime.now()

    #get_stock_info.get_valid_stock_code('60')
#except:
 #   print('something is wrong')
 #   sleep(10)
