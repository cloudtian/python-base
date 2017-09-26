# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#切片slice

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前三个元素
print(L[0:3])
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。
#如果第一个索引是0，还可以省略
print(L[:3])
#倒数切片
print(L[-2:]) #['Bob', 'Jack]
print(L[-2:-1]) #['Bob']  倒数的第一个元素的索引是-1

#创建一个0-99的数列
L = list(range(100))
L[:10] #取前十个
L[-10:] #取后十个
L[:10:2] #前十个数，每两个取一个
L[::5] #所有数，每5个取一个
L[:] #原样复制一个list

#迭代
#for ... in
d = {'a': 1, 'b': 2, 'c': 3}
#迭代key
for key in d:
    print(key)
#迭代value
for value in d.values():
    print(value)
#迭代key和value
for k, v in d.items():
    print(k, ':', v)
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
#字符串也是可迭代对象
for ch in 'ABC':
    print(ch)
#只要作用于一个可迭代对象，for循环就可以正常运行。可通过collections模块的Iterable类型判断一个对象是否为可迭代对象
from collections import Iterable
print('str是否可迭代', isinstance('abc', Iterable)) #str是否可迭代
print('list是否可迭代', isinstance([1, 2, 3], Iterable)) #list是否可迭代
print('整数是否可迭代', isinstance(123, Iterable)) #整数是否可迭代
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#列表生成式 List Comprehensions,是python内置的非常就爱男单却强大的可以用来创建list的生成式
#生成[1,2,3,4,5,6,7,8,9,10]  -->  list[range(1, 11)]
print(list(range(1, 11)))
#生成[1*1,2*2,3*3,...,10*10]
print([x * x for x in range(1, 11)])
#写列表生成式时，要把生成的元素x*x放到前面，后面跟for循环，就可以把list创建出来
#for循环后面还可以加上if判断，例如筛选偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])
#还可以使用两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

#运用列表生成式，可以写出非常简洁的代码，例如，列出当前目录下的所有文件和目录名
import os #导入os模块
print([d for d in os.listdir('.')]) #os.listdir可以列出文件和目录

#使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
#把list中所有字符串都变成小写
print([s.lower() for s in L])

#练习
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
#使用内建的isinstance函数可以判断一个变量是不是字符串：isinstance(x, str)
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)] #str类型的转换成小写，非str类型过滤掉
print(L2)
L3 = [s.lower() if isinstance(s, str) else s for s in L1] #str类型的转换成小写，非str类型的直接返回本身
print(L3)
