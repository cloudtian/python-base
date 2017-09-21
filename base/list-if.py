#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list和tuple 

#list 是一种有序的集合，可以随时添加和删除其中的元素

numberList = [1,2,3,4];
length = len(numberList);

print(numberList)
print(length)

#获取最后一个元素
print(numberList[length-1])
print(numberList[-1])

#追加
numberList.append(5)
print('追加后：' ,numberList)

#把元素插入指定位置，比如索引号为1
numberList.insert(0, 0,)
print('插入索引0：' ,numberList)

#删除
numberList.pop() #删除末尾
print('删除末尾：' ,numberList)
numberList.pop(0) #删除索引0
print('删除索引0：' ,numberList)

#替换
numberList[1] = '2'
print('替换索引1：' ,numberList)

#有序列表元组 tuple, 一旦初始化就不能修改。因为不可变，所以代码更安全
t = (1, 2)
#定义一个元素的tuple
t = (1,)
#t=(1),定义的不是tuple,是1这个数，()既可以表示tuple，也可以表示数学公式中的小括号，所以定义tuple必须加一个逗号
#不可变 是 指向不变，tuple中有list，list里面内容是可以变的，但tuple指向的list这个指向是不变的

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0]) #Apple
print(L[1][1]) #Python
print(L[2][2]) #Lisa

#条件判断
print('please input your age:')
age = int(input());
if age >= 18:
	print('your age is %d, Hello' % age, 'Adult')
elif age >= 6:
	print('your age is %d, Hello' % age, 'teenager')
else: 
	print('your age is %d, Hello' % age, 'kid')

x=[]
if x:
	print('True')
else:
	print('False') #False
	
#练习：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖

height = 1.75
weight = 80.5
bmi = weight/ (height * height)
if bmi > 32:
	print('严重肥胖')
elif bmi > 28:
	print('肥胖')
elif bmi > 25:
	print('过重')
elif bmi > 18.5:
	print('正常')
else:
	print('过轻')


