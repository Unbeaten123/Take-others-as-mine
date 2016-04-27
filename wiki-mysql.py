# -*- coding:utf-8 -*-
#Crawl wikipedia's Urls with a recursionLevel of 4 and then storage them in Mysql

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1',  unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")

#Insert a page if not exist in mysql already
def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

#Insert a link if not exist in mysql already
def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)", (int(fromPageId), int(toPageId)))
        conn.commit()

#Storage Urls without repeat
pages = set()

#Get links that link to a given Url with a recursionLevel no more than 4
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    print "Recursing: ---- http://en.wikipedia.org" + pageUrl
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bs0bj = BeautifulSoup(html, "lxml")
    for link in bs0bj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            #If encounted a new page, add it and search it for links
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage, recursionLevel+1)

#Begin from http://en.wikipedia.org/wiki/Kevin_Bacon
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
connw.close()
