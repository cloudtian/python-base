# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#WSGI:Web Server Gateway Interface
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数
    return [b'<h1>Hello, web!</h1>']
    #函数的返回值作为HTTP响应的Body发送给浏览器

#environ:一个包含所有HTTP请求信息的dict对象
#start_response:一个发送HTTP响应的函数
#start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header,每个Header用一个包含两个str的tuple表示

#Python内置了一个WSGI服务器，这个模块叫wsgiref
#运行WSGI服务
#web/server.py
#web/hello.py
#启动WSGI服务器：python server.py
#浏览器打开：localhost:8000


#使用web框架
#Flask:pip install flash
#同一个URL分别有GET和POST两种请求，映射到两个处理函数中
#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
#web/app.py

#除了Flask，常见的Python Web框架还有：
#Django:全能型Web框架
#web.py:一个小巧的Web框架
#Bottle:和Flask类似的Web框架
#Tornado:Facebook的开源异步Web框架

#使用模块：MVC：Model-View-Controller，中文名“模型-视图-控制器”
#我们把上次直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下
#web/appModule.py

#Flask通过render_template()函数来实现模版的渲染。和Web框架类似，Python的模版也有很多种。
#Flask默认支持的模版是jinja2,安装：pip install jinja2

#除了jinja2，常见的模版还有：
#Mako:用<% ... %>和${xxx}的一个模版
#Cheetah：也是用<% ... %>和${xxx}的一个模版
#Django:Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模版