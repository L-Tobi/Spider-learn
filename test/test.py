import requests
import re
from database import mysql
class America():
    'america stock'

    close = 1
    time = 2
    open = 3
    high = 4
    low = 5
    volumn = 6
    money = 7
    yesterday = 8
    def __init__(self):
        self.database = mysql.America()



    def get_stock_code_summary_info(self):
        url = 'https://hq.sinajs.cn/etag.php?_=1539527704978&list=gb_$dji,gb_ixic'
        result = requests.get(url)
        print (result.text)



        Dji = re.search('dji=".*?,(.*?),.*?,(.*?),.*?,(.*?),(.*?),(.*?),.*?,.*?,(.*?),(.*?),.*,(.*?),.*?";\nvar',result.text,re.S)
        Nasdaq = re.search('xic=".*?,(.*?),.*?,(.*?),.*?,(.*?),(.*?),(.*?),.*?,.*?,(.*?),(.*?),.*,(.*?),.*?";',result.text,re.S)

        recorder_time = Dji.group(America.time)[:10]


        print(Dji.group(America.close), Dji.group(America.time),  Dji.group(America.open), Dji.group(America.high),  Dji.group(America.low), Dji.group(America.volumn),Dji.group(America.money), Dji.group(America.yesterday))
        print(Nasdaq.group(America.close), Nasdaq.group(America.time),  Nasdaq.group(America.open), Nasdaq.group(America.high),  Nasdaq.group(America.low), Nasdaq.group(America.volumn),Nasdaq.group(America.money), Nasdaq.group(America.yesterday))

        # self.database.create_table('America_summary')

        insert_data = (Dji.group(America.open), Dji.group(America.yesterday), Dji.group(America.close), Dji.group(America.high), Dji.group(America.low), Dji.group(America.volumn), Dji.group(America.money)
                       ,Nasdaq.group(America.open), Nasdaq.group(America.yesterday), Nasdaq.group(America.close), Nasdaq.group(America.high), Nasdaq.group(America.low), Nasdaq.group(America.volumn), Nasdaq.group(America.money),recorder_time)
        # self.database.insert_table('America_summary',insert_data)
        a = self.database.find_summary_info(item='time',content='time = ' + recorder_time)

        print(a)


# test = America()
# test.get_stock_code_summary_info()
