# !/usr/bin/env Python3
# -*- coding: utf-8 -*-

#函数式编程 Functional Programming
#高阶函数 Higher-order function

#变量可以指向函数
f = abs
#f <built-in function abs>
#函数本身也可以赋值给变量，即：变量可以指向函数
print(f(-10)) #变量f限制已经指向了abs函数本身，直接调用abs()函数和调用变量f()完全相同

#函数名也是变量
#把abs指向10后，就无法通过abs(-10)调用该函数了
#注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其他模块也生效，
#要用import builtins;builtins.abs = 10

#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))
#编写高阶函数，就是让函数的参数能够接收别的函数

#map/reduce
def f(x):
    return x * x;
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#map()传入的第一个参数是f,即函数对象本身。由于结果r是一个Iterator,Iterator是惰性序列，
#因此通过list()函数让它把整个序列都计算出来并返回一个list

#把每一项转换成字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#对一个序列求和
from functools import reduce
def add(x, y):
    return x + y
print('reduce：' ,reduce(add, [1, 3, 5, 7, 9])) #求和有内建函数sum()
print('sum:', sum([x for x in range(1, 10, 2)]))
