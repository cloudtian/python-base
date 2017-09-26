#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

#生成器generator
#方法1：只要把一个列表生成式的[]改成(),就创建了一个generator
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(g)
#通过next()获取generator的下一个返回值
#每次调用next(g)，就计算出g的下一个元素的值，没有更多的元素时，抛出StopIteration错误
#一般通过for循环迭代，不需要关系StopIteration错误
for n in g:
    print(n)

#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

#要把fib函数变成generator，只需要把print(b)改为 yield b就可以了
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#这个定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就是一个generator
f = fib_g(6)
print(f)

#定义一个generator，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print(next(o))
print(next(o))
print(next(o))
#print(next(o)) #StopInteration

#把函数改成generator后，我们基本不会用next()来获取下一个返回值，而是直接使用for循环来迭代
#但是用for循环调用generator是，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
#必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib_g(6)
while True: 
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#杨辉三角
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

#迭代器iterator
#可以直接作用于for循环的数据类型有：
#集合数据类型：list, tuple, dict, set, str等
#generator，包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
#可以通过isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
print('Iterable')
print('list is Iterable:', isinstance([], Iterable))
print('dirt is Iterable:', isinstance({}, Iterable))
print('str is Iterable:', isinstance('abc', Iterable))
print('generator is Iterable:', isinstance((x for x in range(10)), Iterable))
print('数字 is Iterable:', isinstance(100, Iterable))

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print('Iterator')
print('list is Iterator:', isinstance([], Iterator))
print('dirt is Iterator:', isinstance({}, Iterator))
print('str is Iterator:', isinstance('abc', Iterator))
print('generator is Iterator:', isinstance((x for x in range(10)), Iterator))
print('数字 is Iterator:', isinstance(100, Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print('iter()')
print('list is Iterator:', isinstance(iter([]), Iterator))
print('dirt is Iterator:', isinstance(iter({}), Iterator))
print('str is Iterator:', isinstance(iter('abc'), Iterator))

#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
#Python的for循环本质上就是通过不断调用next()函数实现的