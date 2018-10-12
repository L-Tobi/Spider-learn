import requests
from bs4 import BeautifulSoup
from database import  mysql
current_exchange_rate = 5
current_exchange_rate_date = 6
current_exchange_rate_seconds = 7

last_record_exchange_rate_time = '1990-01-01 00:00:00'

database,database_cursor = mysql.connect_database()

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
    recorder_time = mysql.find_exchange_rate_info(item='max(time)',content='')
    if(str(recorder_time) < last_record_exchange_rate_time):
        mysql.insert_table('exchange_rate_recorder_info', 'exchange_rate', insert_data)
        print ('insert exchange_rate ' ,recorder_time, last_record_exchange_rate_time)


