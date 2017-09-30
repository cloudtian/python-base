#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#错误处理 try...except...finally
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else: #没有错误发生时，会自动执行else语句
    print('no error!')
finally:
    print('finally...')
print('END')

#所有的错误类型都继承自BaseException,所以在使用except时，不但捕获该类型的错误，还把其子类也捕获
#使用try...except捕获错误，可以跨越多层调用
#常见的错误类型和继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

#调用堆栈
#module.err.py
from module.err import main
#main() #查看调用堆栈，python解释器打印错误堆栈，程序被结束

#记录错误
#如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
#既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

# Python内置的logging模块可以非常容易地记录错误信息
#module.err_logging.py
from module.err_logging import main
main() #打印错误信息，正常退出
print('END')
#通过配置，logging可以把错误记录到日志文件里，方便时候排查


#抛出错误
#module.err_raise.py
from module.err_raise import foo
from module.err_raise import FooError
try:
    foo('0')
except FooError as e:
    print('FooError:', e)
print('END')


from module.err_reraise import bar
#bar() #捕获后又上抛

#在bar()函数中，捕获了错误，打印后又把错误通过raise语句抛出去
#捕获错误目的只是记录以下，便于后续追踪。但是由于当前函数不知道应该怎么处理错误，所以，继续上抛，让顶层调用者去处理
#raise语句如果不带参数，就把当前错误原样抛出，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
try:
    10 / 0
except ZeroDivisionError:
    print('input error!')
    #raise ValueError('input error!')#捕获后抛出另一种错误


#调试
#1.print() 将可能有问题的变量打印出来
#2.断言assert
#3.logging
#4.pdb

#assert
print('assert')
def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

#foo1('0')
#启动Python解释器时可以用-O参数来关闭assert, 关闭后，你可以把所有的assert语句当成pass来看

#logging,logging不会抛出错误，而且可以输出到文件
print('logging')
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
#logging级别：debug,info,warning,error, 指定level=INFO,logging.debug就不起作用了，指定level=WARNING后，debug和info就不起作用了

#pdb Python调试器pdb
#以python -m pdb pdb_err.py启动后，pdb定位到下一步要执行的代码。
# 输入命令l来查看代码
# 输入命令n可以单步执行代码
# 输入命令p 变量名 来查看变量
# 输入命令q结束调试

#pdb.set_trace()
#只需import pdb,然后在可能出错的地方放一个pdb.set_trace()就可以设置一个断点
#运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行

#IDE
#如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm


#单元测试
#编写一个Dict类，行为和dict一致，但是可以通过属性来访问
#module.mydict.py
#module.mydict_test.py

#运行单元测试
#1.在最后加入两行代码:
#if __name__ == '__main__':
#    unittest.main()
#2.命令行通过参数-m unittest直接运行单元测试

#setUp与tearDown  这两个方法会分别在每调用一个测试方法的前后分别被执行


#文档测试
#Python内置的文档测试doctest模块可以直接提取注释中的代码并执行测试
#doctest严格按照python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间的一大段烦人的输出
#module.mydict2.py

#练习 对函数fact(n)编写doctest并执行
#module.fact_doctest.py