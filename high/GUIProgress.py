# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#图形界面,Python支持多种图形界面的第三方库：Tk,wxWidgets,Qt,GTK等等
#Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用

#导入Tkinter包的所有内容
from tkinter import *
#从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
    
#pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局

#实例化Application，并启动消息循环
app = Application()
#设置窗口标题
app.master.title('Hello World')
#主消息循环
app.mainloop()

#GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息
#因此，如果消息处理非常耗时，就需要在新线程中处理

#输入文本
from tkinter import *
import tkinter.messagebox as messagebox
class Application2(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
    
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app2 = Application2()
app2.master.title('Hello World')
app2.mainloop()
