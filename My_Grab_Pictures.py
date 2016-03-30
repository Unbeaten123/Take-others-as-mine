import requests
import urllib
import re
import os
from lxml import html

web = raw_input("Enter the url that you want to download pictures: ")

doc = html.parse(web)
title = doc.find('.//title').text

directory = 'F:\\Python_Programs\\Grab_picture\\' + title

if not os.path.exists(directory):
    os.mkdir(directory)
    print "Storage path had been made successfully!"

os.chdir(directory)

a = requests.get(web)
pattern = '''http://[^\s]*\.jpg'''
r = re.findall(pattern, a.content)
print r

count = 0
total = 0

for image_url in r:
    total += 1
    count += 1
    filename = str(count) + '.jpg'
    try:
        urllib.urlretrieve(image_url, filename)
    except:
        print "One picture failed to download!"
    if os.path.getsize(filename) < 51200:
        os.remove(filename)
        count -= 1
        print "%s picture(s) that bigger than 50KB had been successfully downloaded..." % count
print "There are %s pictures totally! %s pictures had been downloaded successfully!" % (total, count)
