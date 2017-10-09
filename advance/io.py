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

#操作文件和目录
#其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数
import os
#操作系统类型:如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

#操作系统中定义的环境变量，全部保存在os.environ这个变量中
print(os.environ)

#获取某个环境变量的值os.environ.get('key')
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

#操作文件和目录的函数一部分放在os模块，一部分放在os.path模块
#查看当前目录的绝对路径
print(os.path.abspath('.'))
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join(os.path.abspath('.'), 'testdir')
#创建一个目录
os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
#删掉一个目录
os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))

#把两个路径合成一个时，不要直接拼字符串，要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
#拆分路径时，也不要直接去 拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分成两个部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/cloudtian/testdir/file.txt'))
#os.path.splitext()可以直接得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

#对文件重命名 os.rename('test.txt', 'test.py')
#删掉文件 os.remove('test.py')

#列出当前目录下所有的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

#利用os模块编写一个能实现dir -l输出的程序。
fileList = [x for x in os.listdir('.')]
for x in fileList:
    print(x)

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def printPath(fileName, path = '.'):
    for x in os.listdir(path):
        newPath = os.path.join(path, x)
        if os.path.isdir(x):
            printPath(fileName, newPath)
        else:
            if x.find(fileName) != -1:
                print(newPath)
printPath('err')

#序列化 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
#把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import pickle #Python提供了pickle模块来实现序列化
d = dict(name='Bob', age=20, score=80)
print(pickle.dumps(d)) #pickle.dumps()方法把任意对象序列化成一个bytes，然后就可以把这个bytes写入文件
#或者另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('file/dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes,然后用pickle.loads()方法反序列化出对象
#也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('file/dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

#把Python对象变成一个JSON
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d)) #dumps()方法返回一个str，内容就是标准的JSON,dump()方法可以直接把JSON写入一个file-like Object
#把JSON反序列化为Python对象，用loads()方法或者对应的load()方法。前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
