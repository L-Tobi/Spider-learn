import requests
import re
import time
import csv
from time import sleep

# https://hq.sinajs.cn/rn=1536422971108&list=s_sh000001,s_sz399001,CFF_RE_IC0,rt_hkHSI,gb_$dji,gb_ixic,b_SX5E,b_UKX,b_NKY,hf_CL,hf_GC,hf_SI,hf_CAD

def get_stock_codes_info():
    code_list = 'https://hq.sinajs.cn/?rn=1534081330022&list='
    with open('sz_code_list.txt','r') as file_code_list:
        index = 0
        while(True):
            current_code = file_code_list.readline()
            if (not current_code):
                code_list = re.sub('\n', '', code_list)
                code_list = code_list[:-1]
                all_codes_info = requests.get(code_list)
                code_results =  all_codes_info.text.split(';')
                for code_item in code_results:
                    if (code_item == '\n'):
                        break
                    code_item_result = re.search('hq_str_.*?(\d+)=".*?,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?', code_item, re.S)
                    print (code_item_result.group(1),code_item_result.group(2),code_item_result.group(3),code_item_result.group(4),code_item_result.group(5),code_item_result.group(6),code_item_result.group(7),code_item_result.group(8),code_item_result.group(9), code_item_result.group(10))

                break
            elif(index == 750):
                index = 0
                code_list = code_list + current_code + ','
                code_list = re.sub('\n', '', code_list)
                code_list = code_list[:-1]
                all_codes_info = requests.get(code_list)
                code_list = 'https://hq.sinajs.cn/rn?=1536422971108&list='
                code_results =  all_codes_info.text.split(';')
                for code_item in code_results:
                    if (code_item == '\n'):
                        break
                    code_item_result = re.search('hq_str_.*?(\d+)=".*?,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?', code_item, re.S)
                    print (code_item_result.group(1),code_item_result.group(2),code_item_result.group(3),code_item_result.group(4),code_item_result.group(5),code_item_result.group(6),code_item_result.group(7),code_item_result.group(8),code_item_result.group(9), code_item_result.group(10))
                sleep(2)
            else:
                code_list = code_list + current_code + ','
                index = index + 1

    # print(code_list)
    # all_codes_info = requests.get(code_list)
    # print (all_codes_info.text)

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

        with open('data/300098' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price','open','yesterday','highest','lowest','volumn','money','turnover','time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sz300098.group(3), 'open': sz300098.group(1),'yesterday' : sz300098.group(2),'highest' : sz300098.group(4),
                             'lowest': sz300098.group(5),'volumn' : sz300098.group(8),'money' : sz300098.group(9),'turnover' : '{0:.5f}'.format(float(sz300098.group(8))/8864398.31),
                             'time': info_time})

        with open('data/300284' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price','open','yesterday','highest','lowest','volumn','money','turnover','time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sz300284.group(3), 'open': sz300284.group(1),'yesterday' : sz300284.group(2),'highest' : sz300284.group(4),
                             'lowest': sz300284.group(5),'volumn' : sz300284.group(8),'money' : sz300284.group(9),'turnover' : '{0:.5f}'.format(float(sz300284.group(8))/5142442.65),
                             'time': info_time})

        with open('data/000001' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price','change','increase','volumn','money','time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sh000001.group(1), 'change': sh000001.group(2),'increase' : sh000001.group(3),'volumn' : sh000001.group(4), 'money': sh000001.group(5), 'time': info_time})

        with open('data/399001' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price', 'change', 'increase', 'volumn', 'money', 'time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sz399001.group(1), 'change': sz399001.group(2),'increase' : sz399001.group(3),'volumn' : sz399001.group(4), 'money': sz399001.group(5), 'time': info_time})

        with open('data/399415' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price', 'change', 'increase', 'volumn', 'money', 'time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sz399415.group(1), 'change': sz399415.group(2),'increase' : sz399415.group(3),'volumn' : sz399415.group(4), 'money': sz399415.group(5), 'time': info_time})

        with open('data/399006' + ' ' + time.strftime("%Y-%m-%d", time.localtime()) + '.csv', 'a',newline='') as csvfile:
            fieldnames = ['price', 'change', 'increase', 'volumn', 'money', 'time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'price': sz399006.group(1), 'change': sz399006.group(2),'increase' : sz399006.group(3),'volumn' : sz399006.group(4), 'money': sz399006.group(5), 'time': info_time})

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