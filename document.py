import urllib2
from io import StringIO
import csv

data = urllib2.urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print dictReader.fieldnames
for row in dictReader:
    print row
