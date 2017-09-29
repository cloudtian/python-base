#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象高级编程 

#使用__slots__
#只允许对Student实例添加name和age属性，为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student1(object):
    __slots__ = ('name', 'age') #用tuple定义运行绑定的属性名称

s = Student1()
s.name = 'cloudtian'
s.age = 23
# s.score = 100  #报错 'Student' object has no attribute 'score'

#注意： __slots__定义的属性尽对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student1):
    pass
g = GraduateStudent()
g.score = 100

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Bill'
s.age = 24
Student.name = 'Michael'
Student.age = 10
Student.score = 89
#s.name = 'Bill' #报错 'Student' object attribute 'name' is read-only
print(s.name, s.age, s.score, Student.name, Student.score)
#如果类变量中与slots中的变量重名，这个类变量将变为read only，在class 定义时会错，然而在class定义之外则不会
#read only会覆盖所有实例的属性，并且在class之外定义的话，以后的实例对象都不能修改实例属性（必须使用类属性）

#使用@property

#普通的get,set
class Student2(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student3(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#还可以定义只读属性，只定义getter方法，不定义setter方法
class Student4(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    
    @property
    def age(self):
        return 2017 - self._birth
#birth是可读写属性，age是只读属性

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

#利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def heigth(self):
        return self._heigth

    @heigth.setter
    def heigth(self, value):
        self._heigth = value
    
    @property
    def resolution(self):
        return self._width * self._heigth

s = Screen()
s.width = 1024
s.heigth = 768
print(s.resolution)

#多重继承
#Animal: Dog狗，Bat蝙蝠，Parrot鹦鹉，Ostrich鸵鸟
class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#Runnable,Flyable功能类
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#各种动物(多重继承)
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

#通常主线都是单一继承下来的，如果需要混入额外功能，可以通过多重继承实现，这种设计通常称为MixIn
#MixIn目的是给一个类增加多个功能
#Python自带了TCPServer和UDPserver两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供
from socketserver import TCPServer
from socketserver import UDPServer
from socketserver import ForkingMixIn
from socketserver import ThreadingMixIn
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


#定制类

#__str__
class Student5(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student5('cloudtian'))
#直接显示变量调用的是__repr__(),__repr__()是为调试服务的
#__str__()返回用户看到的字符串，__repr__()返回程序开发者看到的字符串

#__iter__
#如果一个类想被用于for...in循环，需要实现__iter__()方法，该方法返回一个迭代对象
#Python的for循环会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self #实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a #返回下一个值
for n in Fib():
    print(n)

#__getitem__
#表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib1()
print('f[0]:', f[0])
print('f[10]:', f[10])

#list有切片方法
print(list(range(100))[5:10])
#__getitem__()传入的参数可能是一个int,也可能是一个切片对象
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int): #n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):#n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib2()
print('f[5:10]:', f[5:10])

#如果把对象看成dict,__getitem__()参数也可能是一个可以作key的object
#与之对应的是__setitem__(),把对象视为list或dict来对集合赋值,还有__delitem__()方法，用于删除某个元素

#__getattr__
#正常情况下，当调用类的方法或属性时，如果不存在，就会报错
#当调用不存在的属性时，Python解释器会试图调用__getattr__(self, attr)来尝试获得属性
class Student6(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25 
        print('Student6 object has no attribute：%s' % attr)

s = Student6('cloudtian')
print(s.name)
s.score
print(s.age())
#只有在没有找到属性的情况下，才调用__getattr__，已有的属性不会在__getattr__中查找

#利用完全动态的__getattr__，可以写出一个链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list) #'/status/user/timeline/list'

#__call__
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，用instance.method()来调用
#任何类，只要定义一个__call__方法，就可以直接对是实例进行调用
class Student7(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student7('cloudtian')
s()

#pandaun一个对象是否能被调用，能被调用的对象是一个Callable对象，比如带有__call__()的类实例
print('Student() is callable:', callable(Student()))
print('max function is callable:', callable(max))
print('[1, 2, 3] is callable:', callable([1, 2, 3]))
print('None is callable:', callable('None'))
print('"str" is callable:', callable('str'))

#还要定制方法：https://docs.python.org/3/reference/datamodel.html#special-method-names
