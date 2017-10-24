# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#HTMLParser解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)
    
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    
    def handle_data(self, data):
        print(data)
    
    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)
    
    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
<p>Some <a href=\"#\">html</a> HTML totorial... <br/>END</p>
</body></html>''')
#feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去
#特殊字符有两种，一种是英文表示的&bnsp;一种是数字表示的&#1234;这两种字符都可以通过Parser解析出来

#小结：利用HTMLParser，可以把网页中的文本，图像等解析出来

#练习，找一个网页，例如，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间，名称和地点
