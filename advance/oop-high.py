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
