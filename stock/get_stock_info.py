import requests
import re
import time
import csv
from time import sleep
from database import operation

code_index = 0
code_list = 'https://hq.sinajs.cn/?rn=1534081330022&list='
code_basis_list = 'https://hq.sinajs.cn/?rn=1534081330022&list='
all_code_list = []
all_code_basis_list = []
with open('sz_code_list.txt','r') as file_code_list:
    for code_info in file_code_list:
        if(not code_info):
            print ('end')
        elif(code_index == 700):
            code_index = 0
            current_code = re.sub('\n', '', code_info)
            code_list = code_list + current_code
            code_basis_list = code_basis_list + current_code + '_i'
            all_code_list.append(code_list)
            all_code_basis_list.append(code_basis_list)
            code_basis_list = 'https://hq.sinajs.cn/?rn=1534081330022&list='
            code_list = 'https://hq.sinajs.cn/?rn=1534081330022&list='
        else:
            current_code = re.sub('\n', '', code_info)
            code_list = code_list + current_code + ','
            code_basis_list = code_basis_list + current_code + '_i' + ','
            code_index = code_index + 1
    all_code_list.append(code_list)
    all_code_basis_list.append(code_basis_list)
    # print (all_code_list)
    # print (all_code_basis_list)


def get_stock_codes_info(current_time):
    time_change = True
    minute_data = []
    today_data=[]
    all_code_today_info = {}
    all_code_real_price = {}
    all_code_real_price_temp = {}
    all_code_currcapital = {}
    with open('sz_code_list.txt', 'r') as file_code_list:
        for code_info in file_code_list:
            code_info = re.sub('\n', '', code_info)
            all_code_currcapital[code_info[2:]] = operation.find_stock_basis_info(code_info[2:], 'basis', item='currcapital', content='code_id = ' + code_info[2:])
            all_code_today_info[code_info[2:]] = [0,current_time,100000,current_time]
            all_code_real_price[code_info[2:]] = []
            all_code_real_price_temp[code_info[2:]] = [0,0,current_time]
    while(True):
        for code_list_item in all_code_list:
            current_code_info = requests.get(code_list_item)
            code_results = current_code_info.text.split(';')
            for code_item in code_results:
                if (code_item == '\n'):
                    break
                code_item_result = re.search(
                    'hq_str_.*?(\d+)=".*?,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),.*,(.*?),(.*?),(.*?)',
                    code_item, re.S)
                if (code_item_result == None):
                    continue


                if(time_change):
                    compare_time = code_item_result.group(13) + ' ' + code_item_result.group(14)[:-2] + '59'
                    time_change = False
                record_time = code_item_result.group(13)+' ' + code_item_result.group(14)

                real_time_data = (code_item_result.group(4), code_item_result.group(6), record_time[:-3])
                if(code_item_result.group(1) == '002202'):
                    if (float(code_item_result.group(5)) > all_code_today_info[code_item_result.group(1)][0]):
                        all_code_today_info[code_item_result.group(1)][0] = float(code_item_result.group(5))
                        all_code_today_info[code_item_result.group(1)][1] = record_time[:-3]
                    if(float(code_item_result.group(6)) < all_code_today_info[code_item_result.group(1)][2]):
                        all_code_today_info[code_item_result.group(1)][2] = float(code_item_result.group(6))
                        all_code_today_info[code_item_result.group(1)][3] = record_time[:-3]


                    print(real_time_data , all_code_today_info[code_item_result.group(1)])
                #     记录最高和最低价出现时间
                if(record_time > compare_time):
                    # add data to today
                    time_change = True
                    final_data = (all_code_real_price_temp[code_item_result.group(1)])
                    all_code_real_price[code_item_result.group(1)] = all_code_real_price[code_item_result.group(1)].append(final_data)


                currcapital = all_code_currcapital[code_item_result.group(1)]
                volumn = float(code_item_result.group(9))

                if (currcapital == 0):
                    turnover = 0
                    all_code_real_price_temp[code_item_result.group(1)][1] = turnover
                else:
                    turnover = volumn / currcapital / 100
                    all_code_real_price_temp[code_item_result.group(1)][1] = turnover

                all_code_real_price_temp[code_item_result.group(1)][0] = code_item_result.group(4)
                all_code_real_price_temp[code_item_result.group(1)][2] = record_time[:-3]
                #刷新最高价时对应区间price的数字，并更新进入数据库
                #创建表以年为单位
                # print (code_item_result.group(1), code_item_result.group(2), code_item_result.group(3),
                #        code_item_result.group(4), code_item_result.group(5), code_item_result.group(6),
                #        code_item_result.group(7), code_item_result.group(8), code_item_result.group(9),
                #        code_item_result.group(10),code_item_result.group(13),code_item_result.group(14))

            sleep(2)
        sleep(6)

def get_stock_code_basis_info(is_store_data=False):
    operation.create_table('stock_basis_info','basis')
    for code_list_item in all_code_basis_list:
        current_code_basis_info = requests.get(code_list_item)
        # print (current_code_basis_info.text)
        code_basis_results = current_code_basis_info.text.split(';')
        for code_item in code_basis_results:
            if (code_item == '\n'):
                break
            if(code_item == 'None'):
                continue
            code_item_result = re.search(
                'hq_str_.*?(\d+)_i=".*?,.*?,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?',
                code_item, re.S)
            if (is_store_data):
                insert_data = (code_item_result.group(1), code_item_result.group(2),code_item_result.group(3),
                               code_item_result.group(5), code_item_result.group(7), code_item_result.group(8),
                               code_item_result.group(12), code_item_result.group(13),code_item_result.group(14))
                print (insert_data)
                operation.insert_table('stock_basis_info', 'basis', insert_data)
                # operation.update_stock_basis_info((code_item_result.group(7),code_item_result.group(8),code_item_result.group(1)))
            else:
                print (code_item_result.group(1), code_item_result.group(2), code_item_result.group(3),
                   code_item_result.group(4), code_item_result.group(5), code_item_result.group(6),
                   code_item_result.group(7), code_item_result.group(8), code_item_result.group(9),
                   code_item_result.group(10),code_item_result.group(11),code_item_result.group(12),
                   code_item_result.group(13),code_item_result.group(14),code_item_result.group(15))
        sleep(2)

def get_stock_code_summary_info(is_store_data=False):
    for code_list_item in all_code_list:
        current_code_info = requests.get(code_list_item)
        code_results = current_code_info.text.split(';')
        for code_item in code_results:
            if (code_item == '\n'):
                break
            code_item_result = re.search(
                'hq_str_.*?(\d+)=".*?,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),.*,(.*?),(.*?),(.*?)',
                code_item, re.S)
            if (code_item_result == None):
                continue
            if (is_store_data):

                #open,yesterday,close,high,low,buy,sale,volumn,money
                currcapital = operation.find_stock_basis_info(code_item_result.group(1),'basis',item='currcapital',content='code_id = ' + code_item_result.group(1))

                volumn = float(code_item_result.group(9))
                if (currcapital == 0):
                    turnover = 0
                else:
                    turnover = volumn/currcapital/100
                # print (code_item_result.group(1) , turnover)
                # print (code_item_result.group(1) , ' turnover ' , turnover)
                insert_data = (code_item_result.group(2), code_item_result.group(3), code_item_result.group(4),
                               code_item_result.group(5), code_item_result.group(6), code_item_result.group(7),
                               code_item_result.group(8), code_item_result.group(9), code_item_result.group(10),
                               '{0:.5f}'.format(float(turnover)), code_item_result.group(13))
                # print(insert_data)
                # operation.create_table(code_item_result.group(1) + '_summary', 'summary')
                database_date = operation.find_stock_basis_info(code_item_result.group(1),'summary',item='time',content= 'time = ' + re.sub('-','',code_item_result.group(13)))
                if (database_date == None):
                    operation.insert_table(code_item_result.group(1) + '_summary', 'summary', insert_data)
                else:
                    print ('data has exists, cannot insert repeatly!')
            else:
                print (code_item_result.group(1), code_item_result.group(2), code_item_result.group(3),
                   code_item_result.group(4), code_item_result.group(5), code_item_result.group(6),
                   code_item_result.group(7), code_item_result.group(8), code_item_result.group(9),
                   code_item_result.group(10))
        sleep(2)




'''
    while(True):

    #ready to merge this code
    #responses = requests.get('https://hq.sinajs.cn/rn=1535455880338&list=s_sh000001,s_sz399001,s_sh000300,s_sz399415,s_sz399006')

    code_list = 'https://hq.sinajs.cn/?rn=1534081330022&list=s_sh000001,s_sz399001,s_sh000300,s_sz399006,sz002202,sz300098,sz300284'
    results_list = requests.get(code_list)
    # print(results_list.text)

    sh000001 = re.search('\上证指数,(.*?),(.*?),(.*?),(\d+),(\d+)?', results_list.text, re.S)
    sz399001 = re.search('\深证成指,(.*?),(.*?),(.*?),(\d+),(\d+)?' ,results_list.text, re.S)
    sz399415 = re.search('\沪深300,(.*?),(.*?),(.*?),(\d+),(\d+)?', results_list.text, re.S)
    sz399006 = re.search('\创业板指,(.*?),(.*?),(.*?),(\d+),(\d+)?', results_list.text, re.S)
    sz002202 = re.search('\金风科技,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?).*,(.*?),(.*?),(.*?),.*?"', results_list.text, re.S)
    sz300098 = re.search('\高新兴,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?', results_list.text,re.S)
    sz300284 = re.search('\苏交科,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?', results_list.text, re.S)

    info_time = sz002202.group(12) + ' ' + sz002202.group(13)

    print('002202  now : '.ljust(15) + sz002202.group(3).ljust(10)+ 'open :'.ljust(10) + sz002202.group(1).ljust(10)+ 'yes :'.ljust(10)+ sz002202.group(2).ljust(10)+
          'high :'.ljust(10)+ sz002202.group(4).ljust(10)+ ' low :'.ljust(10) + sz002202.group(5).ljust(10), 'trade vo : '.ljust(10) + sz002202.group(8).ljust(10) +
          'money :'.ljust(6) + sz002202.group(9).ljust(15) + 'turnover rate:'.ljust(12) + '{0:.3f}'.format(float(sz002202.group(8))/28548070.23))
    print('sh cur '.ljust(15)+ sh000001.group(1).ljust(10)+ 'price diff: '.ljust(10) + sh000001.group(2).ljust(10) + 'gr: '.ljust(5) + sh000001.group(3).ljust(10) +
          'trade vo :'.ljust(10) + sh000001.group(4).ljust(10) + 'money :'.ljust(10) + sh000001.group(5).ljust(10) )
    print('sz cur  :'.ljust(15)+ sz399001.group(1).ljust(10)+ 'price diff: '.ljust(10)+ sz399001.group(2).ljust(10)+ 'gr: '.ljust(5)+ sz399001.group(3).ljust(10)+
          'trade vo :'.ljust(10)+ sz399001.group(4).ljust(10)+ 'money :'.ljust(10)+ sz399001.group(5).ljust(10))
    print('hush300 cur:'.ljust(15) + sz399415.group(1).ljust(10)+ 'price diff: '.ljust(10)+ sz399415.group(2).ljust(10)+ 'gr: '.ljust(5)+ sz399415.group(3).ljust(10)+
          'trade vo :'.ljust(10)+ sz399415.group(4).ljust(10)+ 'money :'.ljust(10)+ sz399415.group(5).ljust(10))
    print('300 cur:'.ljust(15) + sz399006.group(1).ljust(10)+ 'price diff: '.ljust(10)+ sz399006.group(2).ljust(10)+ 'gr: '.ljust(5)+ sz399006.group(3).ljust(10)+
          'trade vo :'.ljust(10)+ sz399006.group(4).ljust(10)+ 'money :'.ljust(10)+ sz399006.group(5).ljust(10))
    print('=====================================================================')
    pm_start_time = time.strftime("%Y-%m-%d ", time.localtime()) + '12:57:00'
    pm_end_time = time.strftime("%Y-%m-%d ", time.localtime()) + '15:03:00'
    am_start_time = time.strftime("%Y-%m-%d ", time.localtime()) + '09:23:00'
    am_end_time = time.strftime("%Y-%m-%d ", time.localtime()) + '11:33:00'
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if (current_time > am_start_time and current_time < am_end_time ) or ( current_time > pm_start_time and current_time < pm_end_time):
   # if(True):
        #while item in code_list:

        # with open('data/' + stock_code + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
        #     fieldnames = ['price', 'open', 'yesterday', 'highest', 'lowest', 'volumn', 'money', 'turnover', 'time']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writerow({'price': stock_code.group(3), 'open': stock_code.group(1), 'yesterday': stock_code.group(2),
        #                      'highest': stock_code.group(4),
        #                      'lowest': stock_code.group(5), 'volumn': stock_code.group(8), 'money': stock_code.group(9),
        #                      'turnover': '{0:.5f}'.format(float(stock_code.group(8)) / 28548070.23),
        #                      'time': info_time})




        with open('data/002202' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price','open','yesterday','highest','lowest','volumn','money','turnover', 'time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sz002202.group(3), 'open': sz002202.group(1),'yesterday' : sz002202.group(2),'highest' : sz002202.group(4),
                             'lowest': sz002202.group(5),'volumn' : sz002202.group(8),'money' : sz002202.group(9),'turnover' : '{0:.5f}'.format(float(sz002202.group(8))/28548070.23),
                             'time': info_time})

        # https://hq.sinajs.cn/rn=1535371925672&list=s_sh000001,s_sz399001,CFF_RE_IC0,rt_hkHSI,gb_$dji,gb_ixic,b_SX5E,b_UKX,b_NKY,hf_CL,hf_GC,hf_SI,hf_CAD
        # http://vip.stock.finance.sina.com.cn/quotes_service/view/CN_TransListV2.php?num=11&symbol=sz002202&rn=25589834
        # https://hq.sinajs.cn/rn=1535390045016&list=s_sh000001,s_sz399001,CFF_RE_IC0,rt_hkHSI,gb_$dji,gb_ixic,b_SX5E,b_UKX,b_NKY,hf_CL,hf_GC,hf_SI,hf_CAD
        # https://hq.sinajs.cn/rn=1535455880338&list=s_sh000001,s_sz399001,s_sh000300,s_sz399415,s_sz399006

'''
def get_valid_stock_code(type):
   # codelist = 'sz002202,sz300098,sz300284'
    code_list = 'sh000001,s_sh000001'

    if(type == '00'):
        _index = 0
        sz_code_list = ''
        sz_count = 0
        while _index < 3000:
            url = 'https://hq.sinajs.cn/?rn=1534081330022&list=' + 'sz00' + str(_index).zfill(4)
            results = requests.get(url)
            #print (results.text)
            is_exists = re.search('"(.*)"',results.text ,re.S)

            if(is_exists.group(1) == ''):
                print ('null')
            else:
                print (is_exists.group(1))
                sz_count = sz_count + 1
                sz_code_list += 'sz00' + str(_index).zfill(4)
                with open('sz_code_list.txt', 'a') as file:
                    file.write("sz00" + str(_index).zfill(4) + '\n')
            _index = _index + 1
            sleep(2)
        print (sz_code_list)
        print (' total ' + str(sz_count))
    elif(type == '30'):
        _index = 0
        sz_code_list = ''
        sz_count = 0
        while _index < 1000:
            url = 'https://hq.sinajs.cn/?rn=1534081330022&list=' + 'sz30' + str(_index).zfill(4)
            results = requests.get(url)
            # print (results.text)
            is_exists = re.search('"(.*)"', results.text, re.S)

            if (is_exists.group(1) == ''):
                print ('null')
            else:
                print (is_exists.group(1))
                sz_count = sz_count + 1
                sz_code_list += 'sz30' + str(_index).zfill(4)
                with open('sz_code_list.txt', 'a') as file:
                    file.write("sz30" + str(_index).zfill(4) + '\n')
            _index = _index + 1
            sleep(2)
        print (sz_code_list)
        print (' total ' + str(sz_count))
    elif(type== '60'):
        _index = 0
        sh_code_list = ''
        sh_count = 0
        while _index < 3900:
            url = 'https://hq.sinajs.cn/?rn=1534081330022&list=' + 'sh60' + str(_index).zfill(4)
            results = requests.get(url)
            # print (results.text)
            is_exists = re.search('"(.*)"', results.text, re.S)

            if (is_exists.group(1) == ''):
                print ('null')
            else:
                print (is_exists.group(1))
                sh_count = sh_count + 1
                sh_code_list += 'sh60' + str(_index).zfill(4)
                with open('sz_code_list.txt', 'a') as file:
                    file.write("sh60" + str(_index).zfill(4) + '\n')
            _index = _index + 1
            sleep(2)
        print (sh_code_list)
        print (' total ' + str(sh_count))

    return