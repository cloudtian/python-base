#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#官网查看abs函数文档：https://docs.python.org/3/library/functions.html#abs
#交互式命令行 help(abs) 查看abs函数的帮助信息

#abs绝对值
print('-20的绝对值是：', abs(-20))
#max最大值
print('1,2,3中最大值是：', max(1,2,3))
#数据类型转换
print('int:', int('123'))
print('int:', int(12.34))
print('float:', float('12.34'))
print('str:', str(1.23))
print('bool:', bool(1))
print('bool:', bool(''))

#定义函数 如果没有return语句，函数执行完毕后返回结果None
def my_abs(x):
	#只允许整数或浮点型的参数
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x > 0:
		return x
	else:
		return -x
print('my_abs测试-1', my_abs(-1))
print('my_abs测试2', my_abs(2))
print('my_abs测试-2.1', my_abs(-2.1))
#print('my_abs异常测试-2,1', my_abs(-2,1))
#print('my_abs异常测试"-3"', my_abs("-3"))

#如果已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
#用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）

#空函数
def nop():
	pass
age = 3
if age >= 18:
	pass
#pass可以用来作为占位符，缺少了pass，代码运行就会有语法错误


#返回多个值
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
x,y = move(100,100,60,math.pi/6)
print(x,y)
r = move(100,100,60,math.pi/6)
print(r)
#返回值是一个tuple,在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple,按位置赋给对应的值
#所以，python的函数返回多值其实就是返回一个tuple

#练习:请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
def quadratic(a,b,c):
	if a == 0:
		raise TypeError('a cant be zero')
	if not isinstance(a, (int, float)) and not isinstance(b, (int, float)) and not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	dirta = b**2 - 4*a*c
	if dirta < 0:
		return 
	x = (-b + math.sqrt(dirta)) / (2 * a)
	y = (-b - math.sqrt(dirta)) / (2 * a)
	return x,y

print(quadratic(2,3,1))
print(quadratic(1,3,-4))

#函数的参数
#默认参数 最大的好处是能降低调用函数的难度。默认参数必须指向不变对象
def add_end(L=[]):
	L.append('END')
	return L

print(add_end()) #['END']
print(add_end()) #['END', 'END']
print(add_end()) #['END', 'END', 'END']

#可以用None这个不变对象来实现
def add_end2(L=None):
	if L is None:
		L = []
	L.append('END')
	return L 

#可变参数 在参数前面加了一个*号
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum 

print(calc(1,2))
print(calc())
#如果已经有一个list或tuple
nums = [1,2,3]
print(calc(*nums)) #*nums表示把nums这个list的所有元素作为可变参数传进去

#关键字参数
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, city='Beijing', job='Engineer')

#命名关键字参数
def person(name, age, **kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有job参数
		pass
	print('name:', name, 'age:', age, 'other:', kw)

person('jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如只接受city和job作为关键字参数
def person(name,age,*,city,job):
	print(name,age,city,job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('Jack',24,city='Beijing',job='Engineer')

#参数组合：必选参数，默认参数，可变参数，命名关键字参数，关键字参数
#*args是可变参数，args接收的是一个tuple
#**kw是关键字参数，kw接收的是一个dict
#可变参数既可以直接传入：func(1,2,3)，又可以先组装list或tuple,再通过*args传入：func(*(1,2,3))
#关键字参数既可以直接传入：func(a=1,b=2),又可以先组装dict,再通过**kw传入：func(**{'a'=1,'b'=2})

#递归函数
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
	return fact_iter(n,1)
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1,num*product)
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
#所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

