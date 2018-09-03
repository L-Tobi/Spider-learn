

def get_valid_stock_code():
    codelist = 'sz002202,sz300098,sz300284'
    url = 'https://hq.sinajs.cn/?rn=1534081330022&list=' + codelist
    results = requests.get(url)
    return