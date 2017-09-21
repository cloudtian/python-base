#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#loop循环

#for...in 依次把list或tuple中的每个元素迭代出来
nums = [1, 2, 3, 4]
for num in nums:
	print(num)

#计算1-100的整数之和，range()函数可以生成一个整数序列，再通过list()函数可以转换为list
sum = 0
for x in range(101):
	sum = sum + x
print(sum)#5050

r = range(5)
l = list(r)
print('r:', r, 'l:',l)

#while
#计算100以内所有技术之和
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#练习
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello, %s !' % name)

#break 可以提前退出循环
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END')

#continue 跳出当前这次循环，直接开始下一次循环
#打印0-10奇数
n = 0
while n < 10:
	n = n + 1
	if (n % 2 == 0):
		continue
	print(n)
print('END')

#dict dictionary,(key-value)其他语言也称为map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Michael score: %d' % d['Michael'])

#如果key不存在，dict就会报错
#要避免key不存在的错误：1.通过in判断key是否存在 2.通过dict提供的get方法，如果key不存在，可以返回None,或自己指定的value
print('Thomas is in d ?', 'Thomas' in d)
print('Thomas is in d ?', d.get('Thomas'))
print('Thomas is in d ?', d.get('Thomas', -1))

#删除一个key
print('d:', d)
d.pop('Bob')
print('after delete Bob, d:', d)

#dict和list相比
#dict:1.查找和插入的速度极快，不会随着key的增加而变慢 2.需要占用大量内存，内存浪费多
#list:1.查找和插入随着元素的增加而增加 2.占用空间小，浪费内存很少
#通过key计算位置的算法称为哈希算法（Hash）

#set 和dict类似，也是一组key的集合，但不存储value；由于key不能重复，所以，在set中，没有重复的key
#要创建一个set,需要提供一个list作为输入集合， 重复的元素在set中自动被过滤
s = set([1, 1, 1, 2, 3, 4, 4, 5])
print(s)

s.add(6)
print('add 6:', s)
s.add(6)
print('add 6 again:', s)
s.add(7)
print('add 7:', s)

s.remove(1)
print('remove 1:', s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集，并集等操作
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
print('s1 & s2:', s1 & s2)
print('s1 | s2:', s1 | s2)

#list = [1,2]
#s = set([list, 3])
#print(s)  会报错，set不可以放入可变对象list

tup = (1,2)
s = set([tup, 3])
print(s)  #不会报错，tuple是不可变对象

#tup = (1,2,[3,4])
#s = set([tup, 3])
#print(s)  #会报错，tuple中的list是可变对象

#可变对象
a = ['a', 'c', 'b']
a.sort()
print(a) #['a', 'b', 'c']

#不可变对象
a = 'abc'
a.replace('a', 'A')
print(a) #'abc'

#所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
#相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的










