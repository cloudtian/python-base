#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test hello module' #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'cloudtian' #把作者写出去

import sys #导入sys模块，sys变量指向该模块，利用sys变量可以访问sys模块的所有功能

def test():
    args = sys.argv
    #sys模块有一个argv变量，用list存储了命令行的所有参数，
    #argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    # 如：python3 hello.py获得的sys.argv就是['hello.py']
    # 如：python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__': 
    #当在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
    #而如果在其他地方导入该hello模块时，if判断将失败
    #这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
    test()


#添加一个Hello类
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)