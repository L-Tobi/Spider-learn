from bs4 import BeautifulSoup

def practice_beautifulsoup():
    soup = BeautifulSoup('<p>hello</p>','lxml')
    print(soup.p.string)