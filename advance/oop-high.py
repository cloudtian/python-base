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

#判断一个对象是否能被调用，能被调用的对象是一个Callable对象，比如带有__call__()的类实例
print('Student() is callable:', callable(Student()))
print('max function is callable:', callable(max))
print('[1, 2, 3] is callable:', callable([1, 2, 3]))
print('None is callable:', callable('None'))
print('"str" is callable:', callable('str'))

#还有其他定制方法：https://docs.python.org/3/reference/datamodel.html#special-method-names


#使用枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#获得Month类型的枚举类，通过使用Month.Jan来引用一个常量
for name, member in Month.__members__.items():
    print(name, '=>', member, ',' , member.value)
#value属性是自动赋给成员的int常量，默认从1开始计数

#如果需要更精确的控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 #Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助检查保证没有重复值

#访问枚举类型若干种方法：
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
#print(Weekday(7)) #报错 7 is not a valid Weekday

#Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较


#使用元类
#type()函数可以查看一个类型或变量的类型，Hellow是一个class，它的类型就是type,而h是一个实例，它的类型就是class Hello
#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
from module.hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

#type()函数既可以返回一个对象的类型，又可以创建出新的类型
#如：通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'): #先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) #创建Hello class
h = Hello()
h.hello('cloudtian')
print(type(Hello))
print(type(h))

#创建一个class对象，type()函数依次传入3个参数
#1.class的名称
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
#3.class的名称与函数绑定，这里把函数fn绑定到方法名hello上

#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

#metaclass 元类
#先定义类，然后创建实例；先定义metaclass，然后创建类
#先定义metaclass,就可以创建类，最后创建实例

#metaclass是类的模版，所以必须从type类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
#定义类的时候要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    pass

#__new__()方法接收到的参数依次是：
#1.当前准备创建的类的对象
#2.类的名称
#3.类继承的父类集合
#4.类的方法集合

L = MyList()
print(L)
L.add(1)
print(L)

L2 = list()
#L2.add(1) #报错，普通的list没有add()方法 'list' object has no attribute 'add'
#正常情况下都是直接在MyList定义中添加add()方法

#需要通过metaclass修改类定义的，ORM(Object Relational Mapping) 对象-关系映射
#把关系数据库中的一行映射为一个对象，也就是一个类对应一个表，这样写代码更简单，不用直接操作SQL语句

#定义Field类，负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
#ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model': #1.排除掉对Model类的修改
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items(): #2.在当前类中查找定义的类的所有属性
            if isinstance(v, Field): #如果找到一个Field属性，
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v #就把它保存到一个__mappings__的dict中
        for k in mappings.keys():
            attrs.pop(k) #同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致，把表名保存到__table__中
        return type.__new__(cls, name, bases, attrs)
#基类Model，可以定义各种操作数据库的方法，比如save(),delete(),find(),update()等等
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

#定义一个User类来操作对应的数据库表User
class User(Model):
    #定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

#创建一个实例
u = User(id=12345, name='cloudtian', email='test@orm.org', password='12345')
#保存到数据库
u.save()