# -*- coding: utf-8 -*-
# 导入socket库:
import socket,threading,time

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    print 'Begin the talk'
    while True:
        data = sock.recv(1024)
        print 'Client: ', data
        if data == 'exit' or not data:
            print 'End Talk!'
            time.sleep(2)
            break
        words = raw_input('You: ')
        sock.send(words)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 1500))
s.listen(5)
print 'Waiting for connection...'
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
