#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

#模块
#一个.py文件就称之为一个模块Module
#大大提高代码的可维护性。当一个模块编写完毕，就可以被其他地方引用；可以引用其他模块，包括Python内置的模块和第三方模块
#避免函数名和变量名冲突，相同名字的函数和变量完全可以分别存在不同模块中。
#Python所有内置函数：https://docs.python.org/3/library/functions.html
#为了避免模块名称冲突，Python又引入了按目录来组织模块的方法，称为包Package
#每个包目录下面都会有一个__init__.py文件，这个文件是必须的，否则Python就把这个目录当成普通目录，而不是一个包。
#__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是包含他的文件夹名称

#编写一个hello模块（module.hello）

#作用域
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc,x123,PI等
#类似_xxx和__xxx这样的函数或变量是非公开的（private），不应该被直接引用，比如_abc,__abc等
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


#安装第三方模块，通过包管理工具pip完成; 一般第三方库会在Python官方网站注册：https://pypi.python.org/
#安装第三方库--Python Imaging Libraty，这是Python下非常强大的处理图像的工具库，基于PIL的Pillow项目开发非常活跃
#pip install Pillow

#有了Pillow,处理图片易如反掌，找个图片生成缩略图
from PIL import Image
im = Image.open('img/test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((128, 96))
im.save('img/thumb.jpg', 'JPEG')

#其他常用第三方库：MySQL驱动：mysql-connector-python,用于科学计算的NumPy库：numpy,用于生成文本的模版工具;Jinja2等

#模块搜索路径
#当我们试图加载一个模块式，Python会在指定的路径下搜索对应的.py文件，如果找不到就会报错
#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

#如果我们呀添加自己的搜索目录，有两种方法
#1.直接修改sys.path，添加要搜索的目录
import sys
sys.path.append('./module') #这种方法是在运行时修改，运行结束后失效
#2.设置环境变量PYTHONPATH,该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。
# 注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。