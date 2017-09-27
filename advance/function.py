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

def add2(x, y):
    return x + y
print('reduce：', reduce(add2, [1, 3, 5, 7, 9])) #求和有内建函数sum()
print('sum:', sum([x for x in range(1, 10, 2)]))
#把序列[1,3,5,7,9]变成整数13579
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))

#整理成一个str2int的函数：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

#还可以用lambda函数进一步简化
def str2intLambda(s):
    return reduce(lambda x, y: x * 10, map(char2num, s))

#练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
print('before normalize:', L1)
L2 = list(map(normalize, L1))
print('after normalize:', L2)

#练习，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def ji(x, y):
        return x * y
    return reduce(ji, L)
print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))

#练习：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    def char2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9': 9}[s]
    def fn(x, y):
        return x * 10 + y
    floatLength = len(s.split('.')[1])
    intMod = reduce(fn, map(char2num, s.split('.')[0]))
    floatMod = reduce(fn, map(char2num, s.split('.')[1]))
    return intMod + floatMod * (0.1**floatLength)
print('str2float(\'123.456\') = ', str2float('123.456'))

#filter 用于过滤序列。filter()把传入的函数一次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃

#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
#filter()函数返回的是一个Iterator,也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获取所有结果并返回list

#用filter求素数
#生成器，无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
#生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() #初始化序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) #构造新序列

#打印10以内的素数
for n in primes():
    if n < 10:
        print(n)
    else:
        break

#练习:回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
def is_palindrome(n):
    strNum = str(n)
    result = True
    if len(strNum) % 2 == 0:
        result = False
    else:
        n = 0
        while n < (len(strNum) - 1) / 2:
            if strNum[n] != strNum[-n - 1]:
                result = False
                break
            n = n + 1
    return result 
def is_palindrome2(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))
output = filter(is_palindrome2, range(1, 1000))
print(list(output))

#sorted() 排序函数
print(sorted([36, 5, -12, 9, -21]))
#sorted()函数也是一个高阶函数，可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

#默认情况下，对字符串排序，是按照ASCII的大小比较的

#忽略大小写的排序
print(sorted(['bob', 'ablout', 'Zoo', 'Credit'], key=str.lower))

