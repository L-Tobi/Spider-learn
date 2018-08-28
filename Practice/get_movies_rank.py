import requests
import lxml
from bs4 import BeautifulSoup
from urllib.parse import quote
def get_one_page(url):
    responses = requests.get(url)
    responses.encoding='gbk'
    print(responses.text)
    if  responses.status_code == 200:
        soup = BeautifulSoup(responses.text, 'lxml')
      #  print(soup.prettify())
        return responses.text
    else:
        print('error : ' ,responses.status_code)
    return None

#https://hq.sinajs.cn/rn=1535371925672&list=s_sh000001,s_sz399001,CFF_RE_IC0,rt_hkHSI,gb_$dji,gb_ixic,b_SX5E,b_UKX,b_NKY,hf_CL,hf_GC,hf_SI,hf_CAD
#http://vip.stock.finance.sina.com.cn/quotes_service/view/CN_TransListV2.php?num=11&symbol=sz002202&rn=25589834
#https://hq.sinajs.cn/rn=1535390045016&list=s_sh000001,s_sz399001,CFF_RE_IC0,rt_hkHSI,gb_$dji,gb_ixic,b_SX5E,b_UKX,b_NKY,hf_CL,hf_GC,hf_SI,hf_CAD
#https://hq.sinajs.cn/rn=1535455880338&list=s_sh000001,s_sz399001,s_sh000300,s_sz399415,s_sz399006