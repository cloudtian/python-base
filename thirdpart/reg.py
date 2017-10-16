# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#正则表达式
#精确匹配：\d可以匹配一个数字，\w可以匹配一个字母或数字，.可以匹配任意字符
#*表示任意个字符（包括0个），+表示至少一个字符，?表示0个或1个字符，{n}表示n个字符，{n,m}表示n-m个字符
#[]表示范围，A|B可以匹配A或B，^表示行的开头，$表示行的结束

#re模块
#由于Python的字符串本身也用\转义，如
s1 = 'ABC\\-001' #对应正则表达式字符串：'ABC\-001'
#使用Python的r前缀，就不用考虑转义问题了
s2 = r'ABC\-001' #对应正则表达式字符串：'ABC\-001'
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
#test = input('输入一个带区号的电话号码，以-分隔')
if re.match(r'^\d{3}\-\d{3,8}$', '010-21312'):
    print('输入通过')
else:
    print('输入未通过')

#切分字符串
print('切分字符串split', 'a b   c'.split(' '))
print('切分字符串正则空格', re.split(r'\s+', 'a b   c'))
print('切分字符串正则空格，逗号', re.split(r'[\s+\,]+', 'a,b,  c  d'))
print('切分字符串正则空格，逗号，分号', re.split(r'[\s+\,\;]+', 'a,b;;  c  d'))

#分组
#用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

#贪婪匹配，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r'^(\d+)(0+)$', '102300').groups())
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
#必须让\d+采用非贪婪匹配，才能把后面的0匹配出来，加个?
print(re.match(r'^(\d+?)(0+)$', '102300').groups())

#编译
#当我们在python中使用正则表达式时，re模块内部会干两件事情
#1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错
#2.用编译后的正则表达式去匹配字符串

#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用（编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串）
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

#练习
re_email = re.compile(r'^([\w\.]+@[\w\.]+)$')
print(re_email.match('someone@gmail.com'))
print(re_email.match('bill.gates@microsoft.com'))
re_email2 = re.compile(r'^\<([\w\s]*)\>\s+([\w\.]+@[\w\.]+)$')
print(re_email2.match('<Tom Paris> tom@voyager.org'))
print(re_email2.match('<Tom Paris> tom@voyager.org').groups())
