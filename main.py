from urllib.request import ProxyHandler , build_opener
from finance import stock
from finance import exchange_rate
import sys
import re
import time
import threading
from smtp import mail
from datetime import datetime
from time import sleep
from test import proxy_test
from database import mysql
from tool import debug

pm_start_time = debug.current_time('day') + '13:00:00'
pm_end_time = debug.current_time('day') + '15:01:00'
am_start_time = debug.current_time('day') + '09:25:00'
am_end_time = debug.current_time('day') + '11:31:00'

collect_summary_data = True
#try:
# get_stock_info.get_stock_code_basis_info(True)

exchange_rate_time = datetime.now()

def get_realtime_stock_info():
    while(True):
        current_time = debug.current_time()
        if (current_time > am_start_time and current_time < am_end_time) or (current_time > pm_start_time and current_time < pm_end_time):
            china_stock = stock.China()
            china_stock.get_stock_codes_info(current_time=debug.current_time())
            break
        sleep(50)

thread_realtime = threading.Thread(target=get_realtime_stock_info)
thread_realtime.start()


while(True):
    current_time = debug.current_time()
    if ((datetime.now() - exchange_rate_time).seconds > 300):
        exchange_rate.get_exchange_rate()
        exchange_rate_time = datetime.now()
    sleep(30)
    #get_stock_info.get_valid_stock_code('60')
#except:
 #   print('something is wrong')
 #   sleep(10)
