# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。

#Unix/Linux操作系统提供了一个fork()系统调用
#普通函数调用，调用一次，返回一次，但是fork()调用一次，返回两次
#因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后，分别在父进程和子进程内返回
#子进程永远返回0，父进程返回子进程的ID。
#一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID。而子进程只需要调用getppid()就可以拿到父进程的ID

#windows没有fork调用，下面代码在windows上无法运行
#import os
#print('Process (%s) start...' % os.getpid())
#pid = os.fork()
#if pid == 0:
#    print('I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
#else:
#    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

#multiprocessing模块是跨平台版本的多进程模块
#module.process

#创建子进程时，只需传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

#进程池Pool，需要启动大量的子进程，可以用进程池的方法批量创建子进程
#module.pool

#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了

#子进程，subprocess模块可以方便地启动一个子进程，然后控制其输入和输出
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

#如果子进程还需要输入，可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8')) #这句报错，原因未知
print('Exit code:', p.returncode)

#进程间通信
#Python的multiprocessing模块包装了底层的机制，提供了Queue,Pipes等多种方式来交换数据
#module.queue （报错，原因未知）

#进程是有若干线程组成的，一个进程至少有一个线程，线程是操作系统直接支持的执行单位
#_thread低级模块，threading高级模块，对_thread进行了封装
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading
#新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('threading %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#由于任何进程默认就会启动一个线程，该线程称为主线程，主线程又可以启动新的线程。
#主线程实例的名字叫MainThread，子线程的名字在创建时指定，如果不指定名称，Python就自动命名为Thread-1,Thread-2...
#Python的threading模块有个current_thread()函数，永远返回当前线程的实例

#Lock
#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享
#所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

#假定这是银行存款
balance = 0
def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#加锁
balance = 0
lock = threading.Lock()
def run_thread_lock(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        try:
            #放心修改
            change_it(n)
        finally:
            #改完后释放锁
            lock.release()
t1 = threading.Thread(target=run_thread_lock, args=(5,))
t2 = threading.Thread(target=run_thread_lock, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('after lock:', balance)

#在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
#但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦
#如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象,它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。
#ThreadLocal
import threading
#创建全局的ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
#全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
#你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
#可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

#进程 vs 线程