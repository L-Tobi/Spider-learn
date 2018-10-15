import requests
from bs4 import BeautifulSoup
from database import  mysql
from tool import debug

current_exchange_rate = 5
current_exchange_rate_date = 6
current_exchange_rate_seconds = 7

last_record_exchange_rate_time = '1990-01-01 00:00:00'

database = mysql.ExchangRate()
# mysql.create_table('exchange_rate_recorder_info' ,'exchange_rate')


def get_exchange_rate():
    url = 'http://www.boc.cn/sourcedb/whpj/'
    result = requests.get(url)
    global last_record_exchange_rate_time
    soup = BeautifulSoup(result.text, 'lxml')
    data = []
    for i,th in enumerate( soup.div.find_all(name='tr')):
        if (i > 1  and i < 16) or (i > 16  and  i < 29):
            try:
                current_record_exchange_rate_time = th.find_all(name='td')[current_exchange_rate_date].string + ' ' + th.find_all(name='td')[current_exchange_rate_seconds].string
                data.append(th.find_all(name='td')[current_exchange_rate].string)
                if (current_record_exchange_rate_time != last_record_exchange_rate_time and i == 28):
                    last_record_exchange_rate_time = current_record_exchange_rate_time
                    data.append(current_record_exchange_rate_time)
            except Exception as e:
                print (str(e), i)

    insert_data = tuple(data)
    recorder_time = database.find_realtime_info(item='max(time)',content='')
    if(str(recorder_time) < last_record_exchange_rate_time):
        database.insert_table('exchange_rate_recorder_info', insert_data)
        debug.log_info ('insert exchange_rate ' + str(recorder_time) + str(last_record_exchange_rate_time))


