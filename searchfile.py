# -*- coding: utf-8 -*-
#在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径
#指定字符串和寻找路径参数由命令行给出，路径参数缺省默认为当前目录
# Warning：不要使用F:\或者G:\作为目录会有隐藏文件夹拒绝访问！

import os
import sys

def search(filename, path='.'):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            if filename in i:
                print os.path.join(path, i)
        elif os.path.isdir(os.path.join(path, i)):
            search(filename, os.path.join(path, i))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        search(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 3 or len(sys.argv) < 2:
        print 'Error input, use like this:"python find.py arg1 arg2"'
    else:
        search(sys.argv[1])
