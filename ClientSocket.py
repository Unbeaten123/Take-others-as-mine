# -*- coding: utf-8 -*-
# 导入socket库:
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 1500))
# 接收欢迎消息:
print 'Server: ', s.recv(1024)
print 'Begin the talk'
while True:
    # 发送数据:
    data = raw_input('You: ')
    s.send(data)
    print 'Server: ', s.recv(1024)
s.send('exit')
s.close()
