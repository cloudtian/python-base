# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#协程
#子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

#最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

#用协程实现生产者-消费者模型
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return 
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

#consumer函数是一个generator，把一个consumer传入produce后：
#1.首先调用c.send(None)启动生成器
#2.然后，一旦生成了东西，通过c.send(n)切换到consumer执行
#3.consumer通过yield拿到消息，处理，又通过yield把结果传回
#4.produce拿到consumer处理的结果，继续生产下一条消息
#5.produce决定不生产了，通过c.close()关闭consumer,整个过程结束
#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务


#asyncio是Python3.4版本引入的标准库，直接内置了对异IO的支持
#asyncio的编程模式就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO

import asyncio

#把一个generator标记为coroutine类型，然后就把这个coroutine扔到EventLoop中执行
@asyncio.coroutine
def hello():
    print('Hello world!')
    #异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    #yield from会让我们方便的调用另一个generator
    #由于asyncio.sleep()也是一个coroutine,所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环
    #当asyncio.sleep()返回时，线程就可以从yield from 拿到返回值（此处是None），然后接着执行下一行语句
    print('Hello again!')

#获取EventLoop
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
#loop.close()

import threading

@asyncio.coroutine
def hello2():
    print('Hello2 world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello2 again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello2(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
#loop.close()

#由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
#如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行

#用asyncio的异步网络连接来获取sina,sohu和163的网站首页

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break;
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    #Ignore the body,close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#小结
#asyncio提供了完善的异步IO支持
#异步操作需要在coroutine中通过yield from 完成
#多个coroutine可以封装成一组Task然后并发执行
