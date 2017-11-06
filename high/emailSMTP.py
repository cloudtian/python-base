# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#MUA:Mail User Agent -- 邮件用户代理
#MTA:Mail Transfer Agent -- 邮件传输代理
#MDA:Mail Delivery Agent -- 邮件投递代理
#电子邮件的旅程：发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

#编写程序来发送和接收邮件的本质是：
#1.编写MUA把邮件发到MTA
#2.编写MUA从MDA上收邮件
#发邮件时，MUA和MTA使用的协议就是SMTP:Simple Mail Transfer Protocol,后面的MTA到另一个MTA也是用SMTP协议
#收邮件时，MUA和MDA使用的协议有两种:POP:Post Office Protocol，目前版本是3，俗称POP3;
# IMAP:Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱等等。

#SMTP发送邮件
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件,smtplib负责发送邮件

#from email.mime.text import MIMEText
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype,传入plain表示纯文本，最终的MIME就是text/plain,最后一定要utf-8编码保证多语言兼容性

#输入Email地址和口令：
#from_addr = input('From:')
#password = input('Password:')
#输入收件人地址
#to_addr = input('To:')
#输入SMTP服务器地址
#smtp_server = input('SMTP server:')

#import smtplib
#server = smtplib.SMTP(smtp_server, 25)#SMTP协议默认端口是25
#server.set_debuglevel(1)
#server.login(from_addr, password)
#server.sendmail(from_addr, [to_addr], msg.as_string())
#server.quit()

#用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#SMTP协议就是简单的文本命令和响应。
#login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list,邮件正文是一个str，as_string()把MIMEText对象变成str

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

try:
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')

#发送HTML邮件
#构造MIMEText对象时，把HTML字符串传进去，再把第二个参数有plain变为html就可以了
msg = MIMEText('<html><body><h1>Hello</h1>' + 
'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
'</body></html>', 'html', 'utf-8')

#发送附件
#可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象

#邮件对象
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

#邮件正文是MIMEText
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

#添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('img/test.jpg', 'rb') as f:
    #设置附件的MIME和文件名
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', 0)
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart
    msg.attach(mime)


#发送图片
#把MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片
#在html中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + 
'<p><img src="cid:0"></p>' +
'</body></html>', 'html', 'utf-8'))

#同时支持HTML和Plain格式
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

#加密SMTP
#先创建SSL安全连接，然后再使用SMTP协议发送邮件。
#Gmail的SMTP端口是587
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
#剩下的代码和前面一模一样
server.set_debuglevel(1)
#只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。

#构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，
# 要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
#Message
#+- MIMEBase
#   +- MIMEMultipart
#   +- MIMENonMultipart
#      +- MIMEMessage
#      +- MIMEText
#      +- MIMEImage
