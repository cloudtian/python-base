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
#反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

#练习 假设用一组tuple表示名称和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#用sorted()对上述列表分别按名称排序
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
print('sorted by name:', sorted(L, key=by_name))
print('sorted by score:', sorted(L, key=by_score))


#返回函数
#函数作为返回值
#可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
#如果不需要立刻求和，可以不返回求和结果而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2) #False

#闭包
def count1():
    fs = []
    for i in range(1, 4): #[1, 2, 3]
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count1()
print(f1()) #9
print(f2()) #9
print(f3()) #9
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量:再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count2()
print(f1()) #1
print(f2()) #4
print(f3()) #9
#缺点是代码较长，可利用lambda函数缩短代码
def count3():
    return [(lambda x:(lambda : x*x))(i) for i in range(1, 4)]
f1, f2, f3 = count3()
print(f1()) #1
print(f2()) #4
print(f3()) #9


#匿名函数
#匿名函数lambda x: x * x 实际上就是：
def f(x):
    return x * x;
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
f = lambda x: x * x
print(f)
print(f(5))

def build(x, y):
    return lambda: x * x + y * y
f = build(2, 3)
print(f)
print(f())

def multipliers():
    return [lambda x: i * x for i in range(4)]
print([m(2) for m in multipliers()])


#装饰器 Decorator
#函数对象有一个__name__属性，可以拿到函数的名字
def now1():
    print('2017-9-28')
f = now1
print(now1.__name__)
print(f.__name__)
#增加now()函数的功能，比如：在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称为“装饰器”
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        result = func(*args, **kw)
        print('after call %s():' % func.__name__)
        return result
    return wrapper

#借助Python的@语法，把decorator置于函数的定义处
@log
def now2():
    print('2017-9-28')
now2()
print(now2.__name__)#wrapper
#把@log放到now2()函数的定义处，相当于执行了语句 now = log(now)
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            result = func(*args, **kw)
            print('after %s %s():' % (text, func.__name__))
        return wrapper
    return decorator
@log2('execute')
def now3():
    print('2017-9-28')
now3()
print(now3.__name__)#wrapper
#经过decorator装饰之后的函数，__name__已经从原来的now变成了wrapper
#需要使用Python内置的functools.wraps
import functools
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'% (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#练习：能在函数调用的前后打印出'begin call'和'end call'的日志
def log5(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin %s %s():' % (text, func.__name__))
            resultFn = func(*args, **kw)
            print('end %s %s():' % (text, func.__name__))
            return resultFn
        return wrapper
    return decorator
@log5()
def f():
    print('test log5()')
f()
@log5('execute')
def f2():
    print('test log5(execute)')
f2()
@log5('execute')
def add(x, y):
    print('x = ', x, ',y = ', y)
    return x + y
print('1 + 2 =', add(1, 2))


#偏函数 Partial function 
#functools.partial就是帮助创建偏函数的
import functools
int2 = functools.partial(int, base=2)
print(int2('1010101'))
#functools.partial作用：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
print(int2('1010101', base=10)) #也可以在函数调用时传入其他值

