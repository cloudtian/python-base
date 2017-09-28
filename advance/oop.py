#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象编程 Object Oriented Programming,简称OOP\

#处理学生成绩表

#面向过程实现：
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 88}
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
print_score(std1)
print_score(std2)
#面向对象实现
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

#类和实例
class ClassName(object):
    pass
#class后面紧接着是类名，类名通常大写开头，紧接着是(object)，表示该类从哪个类继承下来
#创建实例是通过类名+()实现的 bart = Student()

#创建实例时，可以把一些必须绑定的属性强制填进去。通过特殊的__init__方法
#__init__方法的第一个参数永远是self，表示创建的实例本身


#数据封装
#这些封装数据的函数是和类本身关联起来的，称之为类的方法
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

#访问限制
#如果让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在python中，实例的变量名如果以__开头，就变成了一个私有变量
#只有内部可以访问，外部不能访问
class Student3(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student3('Bart Simpson', 98)
#print(bart.__name) #报错， 这样就确保了外部代码不能随意修改对象内部的状态，通过访问限制的保护，代码更加健壮
#外部要获取或修改，添加set，get方法
class Student4(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

#注意：Python中，变量名类似__xx__的，是特殊变量，特殊变量是可以直接访问的，不是private变量
#一个下划线开头的实例变量名：_xx，这样的实例变量外部是可以访问的。一般意思是“虽然我可以被访问，但把我视为私有变量，不用随意访问”

#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

animal = Animal()
animal.run()

class Dog(Animal):
    pass

dog = Dog()
dog.run() #直接继承了父类的run方法

class Cat(Animal):
    def run(self): #子类的run()覆盖父类的run()，多态
        print('Cat is running')
    def eat(self):
        print('Eating fish...')
cat = Cat()
cat.run()
cat.eat()

#在继承关系中，如果一个实例的数据类型是某个子类，那么它的数据类型也可以被看做是父类，反过来则不行
print('cat is Cat:', isinstance(cat, Cat))
print('cat is Animal:', isinstance(cat, Animal))
print('animal is Cat:', isinstance(animal, Cat))


#获取对象信息
#使用type()来判断对象类型
#基本类型都可以用type()判断,如果一个变量指向函数或者类，也可以用type()判断
print(type(123))
print(type(123.4))
print(type('str'))
print(type(None))
print(type(abs))
print(type(cat))

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
print(type('abc') == str)
print(type(123) == int)

import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#对于class的继承关系来说，使用type()很不方便， 可以使用isinstance()函数
#能用type()pandaun的基本类型也可以用isinstance()判断
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
#并且可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

#如果要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
#__xxx__的属性和方法在Python中都是有特殊用途的
#__len__返回长度，如果调用len()函数，它会自动调用该对象的__len__()方法
print("len('ABC') == 'ABC'.__len__():", len('ABC') == 'ABC'.__len__())

#自己写的类，如果想用len(myObj)，可以自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print('dog len:', len(dog)) 

#配合getattr(),setattr(),hasattr()可以操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
#测试该对象的属性
print('obj has attr x:', hasattr(obj, 'x'))
print(obj.x)
print('obj has attr y:', hasattr(obj, 'y'))
setattr(obj, 'y', 10)
print('after set obj attr y, obj has attr y:', hasattr(obj, 'y'))
print('get obj attr y:', getattr(obj, 'y'))

#如果获取不存在的属性，会抛出AttributeError错误
#可以传入一个default参数，如果属性不存在就返回默认值
print('get obj attr z:', getattr(obj, 'z', 'None'))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
print(getattr(obj, 'power')())

def readImage(fp):
    if hasattr(fp, 'read'):
        return fp.read()
    return None

#实例属性和类属性
class Student5(object):
    name = 'Student' #类属性

s = Student5()
s.score = 90 #实例属性
print(s.name)
print(Student5.name)
s.name = 'cloudtian'
print(s.name)
print(Student5.name)
del s.name #删除实例的name属性
print(s.name)