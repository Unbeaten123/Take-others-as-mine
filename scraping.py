import urllib2
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import re

def getnamelist(url):
    namelist = []
    try:
        html = urllib2.urlopen(url)
    except HTTPError:
        return None
    try:
        bs0bj = BeautifulSoup(html, 'lxml')
        for link in bs0bj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
            if 'href' in link.attrs:
                namelist.append(link.attrs['href'])
    except AttributeError as e:
        return None
    return namelist

nameList = getnamelist('http://en.wikipedia.org/wiki/Kevin_Bacon')
if nameList == None:
    print 'nameList could not be found!'
else:
    for name in nameList:
        print name
