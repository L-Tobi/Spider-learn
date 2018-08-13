from lxml import etree

def practice_lxml_test(url):
    html = etree.parse(url, etree.HTMLParser())
 #   result = etree.tostring(html)
  #  print(result.decode('utf-8'))
    return