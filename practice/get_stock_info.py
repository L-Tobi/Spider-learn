import requests
import re
def get_stock_start(url):
    responses = requests.get('https://hq.sinajs.cn/rn=1535455880338&list=s_sh000001,s_sz399001,s_sh000300,s_sz399415,s_sz399006')
    shanghai = re.search('\上证指数,(.*?),(.*?),(.*?),(\d+),(\d+)?', responses.text, re.S)
    shenzhen = re.search('\深证成指,(.*?),(.*?),(.*?),(\d+),(\d+)?' ,responses.text, re.S)
    hushen300 = re.search('\沪深300,(.*?),(.*?),(.*?),(\d+),(\d+)?', responses.text, re.S)
    chuangye = re.search('\创业板指,(.*?),(.*?),(.*?),(\d+),(\d+)?', responses.text, re.S)

    url002202 = 'https://hq.sinajs.cn/?rn=1534081330022&list=sz002202,sz002202_i'
    responses002202 = requests.get(url002202)
   # print(responses002202.text)
    sz002202 = re.search('\金风科技,(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)?', responses002202.text, re.S)
    print(sz002202)
    print('002202  now : ', sz002202.group(3), ' open :' , sz002202.group(1), ' yes :' , sz002202.group(2), ' high :', sz002202.group(4), ' low :' , sz002202.group(5))
    print('sh cur         ', shanghai.group(1), '   price diff: ', shanghai.group(2), '   gr: ', shanghai.group(3),
          '     trade vo :', shanghai.group(4), ' money :', shanghai.group(5))
    print('hz cur         ', shenzhen.group(1), '        price diff: ', shenzhen.group(2), '     gr: ', shenzhen.group(3),
          '      trade vo :', shenzhen.group(4), ' money :', shenzhen.group(5))
    print('hush300 cur    ', hushen300.group(1), '   price diff: ', hushen300.group(2), '    gr: ', hushen300.group(3),
          '     trade vo :', hushen300.group(4), ' money :', hushen300.group(5))
    print('300 cur        ', chuangye.group(1), '        price diff: ', chuangye.group(2), '     gr: ', chuangye.group(3),
          '     trade vo :', chuangye.group(4), ' money :', chuangye.group(5))
    print('=====================================================================')