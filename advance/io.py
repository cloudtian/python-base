#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#IO编程
#IO -> Input/Output 输入和输出
#Stream流，只能单向流动。Input Stream就是数据从外面(磁盘，网络)流进内存，Output Stream就是数据从内存流到外面。
#对浏览网页来说，浏览器和服务器之间至少需要建立两个流，才能既发数据，又能接收数据

#同步IO,异步IO  区别在于是否等待IO执行的结果。异步IO的复杂度远远高于同步IO。

#文件读写
#要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
f = open('file/text.txt', 'r') 
#标示符'r'表示读
#如果文件不存在就会抛出一个IOError的错误

#调用read()方法可以一次读取文件的全部内容，Python把内存读到内存，用一个str对象表示
print(f.read())

#调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()

#由于文件读写时都有可能产生IOError，一旦出错f.close()就不会调用，所以为了保证无论是否出错都能正确地关闭文件，可以使用try...finally
try:
    f = open('file/text.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#Python引入了with语句来自动帮我们调用close()方法：
with open('file/text.txt', 'r') as f:
    print(f.read())

#read(size)：每次最多读取size个字节的内容
#readline()：每次读取一行内容
#readlines():一次读取所有内容并按行返回list
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('file/text.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) #把末尾的'\n'删掉

#file-like Object:  像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲

#二进制文件
#要读取二进制文件，比如图片，视频等等，用'rb'模式打开文件即可
with open('img/io_test.jpg', 'rb') as f:
    print(f.read())

#字符编码
#读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#f = open('file/gbk.txt', 'r', encoding='gbk')
#遇到编码不规范的文件，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
#f = open('file/xxx.txt', 'r', encoding='gbk', errors='ignore')

#写文件
#标识符'w'或者'wb'表示写文本文件或写二进制文件
with open('file/write.txt', 'w') as f:
    f.write('write something into file by code')


#内存读写 StringIO
#StringIO就是内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue()) 
#getValue()方法用于获得写入后的str
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#二进制数据读写 BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#注意：写入的不是str，而是经过UTF-8编码的bytes
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
