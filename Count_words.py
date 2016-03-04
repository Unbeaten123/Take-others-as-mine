# coding=utf-8
import re
from collections import Counter

textpath = raw_input("Enter the path of a text file: ")

'''函数：输入一个英文的纯文本文件，统计其中单词个数'''
def getMostCommonWord(articlefilesource):
    pattern = '''[A-Za-z]+'''
    f = open(articlefilesource)
    r = re.findall(pattern,f.read())
    '''只返回10个频度最高的单词'''
    return Counter(r).most_common(10)

wordtuple = getMostCommonWord(textpath)

for entity in wordtuple:
    print entity
