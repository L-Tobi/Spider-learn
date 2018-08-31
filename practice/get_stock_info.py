import requests
import re
import time
def get_stock_start(url):

    responses = requests.get('https://hq.sinajs.cn/rn=1535455880338&list=s_sh000001,s_sz399001,s_sh000300,s_sz399415,s_sz399006')
    shanghai = re.search('\上证指数,(.*?),(.*?),(.*?),(\d+),(\d+)?', responses.text, re.S)
    shenzhen = re.search('\深证成指,(.*?),(.*?),(.*?),(\d+),(\d+)?' ,responses.text, re.S)
    hushen300 = re.search('\沪深300,(.*?),(.*?),(.*?),(\d+),(\d+)?', responses.text, re.S)
    chuangye = re.search('\创业板指,(.*?),(.*?),(.*?),(\d+),(\d+)?', responses.text, re.S)

    url002202 = 'https://hq.sinajs.cn/?rn=1534081330022&list=sz002202,sz002202_i'
    responses002202 = requests.get(url002202)
   # print(responses002202.text)
    sz002202 = re.search('\金风科技,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?', responses002202.text, re.S)


    print('002202  now : '.ljust(15) + sz002202.group(3).ljust(10)+ 'open :'.ljust(10) + sz002202.group(1).ljust(10)+ 'yes :'.ljust(10)+ sz002202.group(2).ljust(10)+
          'high :'.ljust(10)+ sz002202.group(4).ljust(10)+ ' low :'.ljust(10) + sz002202.group(5).ljust(10), 'trade vo : '.ljust(10) + sz002202.group(8).ljust(10) +
          'money :'.ljust(6) + sz002202.group(9).ljust(15) + 'turnover rate:'.ljust(12) + '{0:.3f}'.format(float(sz002202.group(8))/28548070.23))
    print('sh cur '.ljust(15)+ shanghai.group(1).ljust(10)+ 'price diff: '.ljust(10) + shanghai.group(2).ljust(10) + 'gr: '.ljust(5) + shanghai.group(3).ljust(10) +
          'trade vo :'.ljust(10) + shanghai.group(4).ljust(10) + 'money :'.ljust(10) + shanghai.group(5).ljust(10) )
    print('sz cur  :'.ljust(15)+ shenzhen.group(1).ljust(10)+ 'price diff: '.ljust(10)+ shenzhen.group(2).ljust(10)+ 'gr: '.ljust(5)+ shenzhen.group(3).ljust(10)+
          'trade vo :'.ljust(10)+ shenzhen.group(4).ljust(10)+ 'money :'.ljust(10)+ shenzhen.group(5).ljust(10))
    print('hush300 cur:'.ljust(15) + hushen300.group(1).ljust(10)+ 'price diff: '.ljust(10)+ hushen300.group(2).ljust(10)+ 'gr: '.ljust(5)+ hushen300.group(3).ljust(10)+
          'trade vo :'.ljust(10)+ hushen300.group(4).ljust(10)+ 'money :'.ljust(10)+ hushen300.group(5).ljust(10))
    print('300 cur:'.ljust(15) + chuangye.group(1).ljust(10)+ 'price diff: '.ljust(10)+ chuangye.group(2).ljust(10)+ 'gr: '.ljust(5)+ chuangye.group(3).ljust(10)+
          'trade vo :'.ljust(10)+ chuangye.group(4).ljust(10)+ 'money :'.ljust(10)+ chuangye.group(5).ljust(10))
    print('=====================================================================')
    pm_start_time = time.strftime("%Y-%m-%d ", time.localtime()) + '12:57:00'
    pm_end_time = time.strftime("%Y-%m-%d ", time.localtime()) + '15:03:00'
    am_start_time = time.strftime("%Y-%m-%d ", time.localtime()) + '09:13:00'
    am_end_time = time.strftime("%Y-%m-%d ", time.localtime()) + '11:33:00'
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if (current_time > am_start_time and current_time < am_end_time ) or ( current_time > pm_start_time and current_time < pm_end_time):
        file = open('data/002202' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.txt', 'a+')
        file.write(sz002202.group(3) + ' ' + sz002202.group(8) + ' ' + sz002202.group(9) + ' ' + '{0:.5f}'.format(float(sz002202.group(8))/28548070.23) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 002202'+ '\n')
        file.write(shanghai.group(1) + ' ' + shanghai.group(2) + ' ' + shanghai.group(3) + ' ' + shanghai.group(
            4) + ' ' + shanghai.group(5) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' shanghai' + '\n')
        file.write(shenzhen.group(1) + ' ' + shenzhen.group(2) + ' ' + shenzhen.group(3) + ' ' + shenzhen.group(
            4) + ' ' + shenzhen.group(5) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' shenzhen'+ '\n')
        file.write(hushen300.group(1) + ' ' + hushen300.group(2) + ' ' + hushen300.group(3) + ' ' + hushen300.group(
            4) + ' ' + hushen300.group(5) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' hushen300' + '\n')
        file.write(chuangye.group(1) + ' ' + chuangye.group(2) + ' ' + chuangye.group(3) + ' ' + chuangye.group(
            4) + ' ' + chuangye.group(5) + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' chuanye'+ '\n')
        file.close()