# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#网络编程：网络通信就是两个进程之间在通信
#TCP/IP
#互联网上每个计算机的唯一标识就是IP地址，类似123.123.123.123。
#如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，所以，IP地址对应的实际上是计算机的网络接口，通常是网卡。

#IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。
# 由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。
# IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。

#IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的是便于阅读。

#IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于2001:0db8:85a3:0042:1000:8a2e:0370:7334

#TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
#TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

#一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口

#一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。


#TCP编程

#客户端
#大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

#导入socket库
import socket
#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn', 80)) #注意参数是一个tuple，包含地址和端口号
#创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议。
#端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

#建立TPC连接后，就可以像新浪服务器发送请求，要求返回首页内容
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
    #每次最多接收1k字节
    d = s.recv(1024)#接收数据时，调用recv(max)方法，一次最多接收指定的字节数。因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#关闭连接
s.close()
#接收到的数据包括HTTP头和网页本身
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
#把接收的数据写入文件：
with open('sina.html', 'wb') as f:
    f.write(html)


#服务器
#服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
#服务器需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或新的线程来处理，否则，服务器一次就只能服务一个客户端了。

f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5) #传入参数指定等待连接的最大数量
print('Waiting for connection...')

