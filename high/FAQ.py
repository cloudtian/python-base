#-*- coding:utf-8 -*-
#常见问题：

#如何获取当前路径
#当前路径可以用'.'表示，再用os.path.abspath()将其转换为绝对路径
import os
print(os.path.abspath('.'))

#如何获取当前模块的文件名
#可以通过特殊变量__file__获取
print(__file__)

#如何获取命令行参数
#可以通过sys模块的argv获取
import sys
print(sys.argv)
#argv的第一个元素永远是命令行执行的.py文件名

#如何获取当前Python命令的可执行文件路径
#sys模块的executable变量就是Python命令可执行文件的路径
print(sys.executable)


