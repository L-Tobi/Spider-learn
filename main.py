from finance import stock
from finance import exchange_rate
import threading
from datetime import datetime
from time import sleep
from tool import debug


exchange_rate_time = datetime.now()

def get_realtime_stock_info():
    while(True):
        current_time = debug.current_time()
        am_start_time = debug.current_time('day') + ' 09:29:00'
        am_end_time = debug.current_time('day') + ' 15:03:00'
        if (current_time > am_start_time and current_time < am_end_time):
            china_stock = stock.China()
            china_stock.get_stock_codes_info()
        sleep(30)

thread_realtime = threading.Thread(target=get_realtime_stock_info)
thread_realtime.start()


while(True):
    current_time = debug.current_time()
    if ((datetime.now() - exchange_rate_time).seconds > 300):
        exchange_rate.get_exchange_rate()
        exchange_rate_time = datetime.now()
    sleep(10)