# coding=utf-8
import re
from collections import Counter

textpath = raw_input("Enter the path of a text file: ")

def getMostCommonWord(articlefilesource):
    '''输入一个英文的纯文本文件，统计其中的单词出现的个数'''
    pattern = '''[A-Za-z]+|\$?\d+%?$'''
    f = open(articlefilesource)
    r = re.findall(pattern,f.read())
    return Counter(r).most_common()

wordtuple = getMostCommonWord(textpath)

'''输出频度最高的5个单词'''
count = 0
for entity in wordtuple:
    print entity
    count += 1
    if count == 5:
        break
