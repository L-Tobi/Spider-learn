from lxml import etree

def practice_lxml_test(url):
    html = etree.parse(url, etree.HTMLParser())
    #result = html.xpath('//td/text()')
    result = html.xpath('//table[@border="0"]/tbody/tr/td/text()')
    #result = etree.tostring(html)
    print(result)
    #print(result.decode('utf-8'))
    return