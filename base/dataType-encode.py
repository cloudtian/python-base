#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#base
#当语句以冒号:结尾时，缩进的语句视为代码块 坚持使用4个空格的缩进
#Python程序是大小写敏感的

#数据类型和变量
print('整数：', 1, 100)
print('浮点数：', 1.23, 3.14)
#整数运算永远是精确的，浮点数运算则可能会有四舍五入的误差
print('字符串：', 'abc', 'I\'m ok', "I'm ok")
#r''表示''内部的字符串默认不转义  '''...'''格式表示多行内容
print('\\\n\\')
print(r'\\\n\\')
print('''line1
line2
line3''')
#布尔值，and or not 运算
print('True', 'False')
age = int(input('please input a age number:'))
if age >= 120 or age <= 0:
	print('you are not human')
elif age >= 60:
	print('you are an old man')
elif age >= 18:
	print('you are an adult')
elif age >= 14:
	print('you are a teenager')
elif age >= 6:
	print('you are a child')
else:
	print('you are a baby')
	
#空值None
#变量
a = 'ABC'#1.内存中创建一个'ABC'字符串，2.在内存中创建一个名为a的变量，并把它指向'ABC'
b = a;#变量b指向变量a所指向的数据，即字符串'ABC'
a = 'XYZ'#解释器创建字符串'XYZ',并把a的指向改为'XYZ',但b并没有改
print(b)
#常量
PI = 3.14159265359
print('10 / 3 =', 10 / 3) #3.333333333
print('9 / 3 =', 9 / 3) #3.0
print('10 // 3 =', 10 // 3) #3
print('10 % 3 =', 10 % 3) #1

#练习 打印以下变量的值
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)

#string
#编码：
#ASCII编码（127个字符，大小写英文字母，数字，符号）通常是1个字节
#GB2312编码（中国制定的，处理中文）
#Unicode（所有语言统一处理）通常是2个字节
#UTF-8（用Unicode编码比ASCII编码多一倍存储空间，本着节约精神，把Unicode编码转化为"可变长编码"UTF-8）
#   UTF-8编码把一个Unicode字符根据不同数字大小编码成1-6个字节，常用英文字母1个字节，汉字通常3个字节，只有很生僻字符4-6个字节。

#!/usr/bin/env python3  
#-*- coding: utf-8 -*- 
##第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，windows系统会忽略这个注释
##第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

#格式化
# %d 整数， %f 浮点数， %s 字符串， %x 十六进制整数

#练习 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
r = (s2-s1)/s1 * 100
print('%.1f %%' %r)

