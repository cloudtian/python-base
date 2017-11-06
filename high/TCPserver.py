# -*- coding:utf-8 -*-

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5) #传入参数指定等待连接的最大数量
print('Waiting for connection...')


#每个连接都必须创建新线程或进程来处理，否则，单线程在处理连接的过程中，无法接收其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    #接受一个新连接
    sock, addr = s.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()