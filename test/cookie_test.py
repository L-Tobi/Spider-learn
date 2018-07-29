from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

def check_robot_txt(url):
    rp = RobotFileParser(url+ '/robots.txt')
    rp.read()
  #  rp.parse(urlopen(url.read().decode('utf-8').split('\n')))
    print(rp.can_fetch('*', url + '/stock/'))
    return