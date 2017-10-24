# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#除了内建的模块外，Python还有大量的第三方模块
#基本上，所有的第三方模块都会在https://pypi.python.org/上注册，只要找到对应的模块名字，即可用pip安装

#PIL:Python Imaging Library
#由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

#安装Pillow: pip install pillow

#操作图像
#图像缩放
from PIL import Image
#打开一个jpg图像文件
im = Image.open('img/test.jpg')
#获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
#缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
#把缩放后的图像用jpeg格式保存
im.save('img/thumbnail.jpg', 'jpeg')

#其他功能，如切片，旋转，滤镜，输出文字，调色板等一应俱全
#模糊
from PIL import Image, ImageFilter
im = Image.open('img/test.jpg')
#应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
print('image blur')
im2.save('img/blur.jpg', 'jpeg')
im3 = im.filter(ImageFilter.EDGE_ENHANCE)
print('image edgeEnhance')
im3.save('img/edgeEnhance.jpg', 'jpeg')


#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图，比如要生成字母验证码图片
print('start生成验证码图片')
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65, 90))
#随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
#创建Font对象
font = ImageFont.truetype('arial.ttf', 36)
#创建Draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
#输出文字
for t in range(4):
    ch = rndChar()
    print(ch)
    draw.text((60 * t + 10, 10), ch, font=font, fill=rndColor2())
#模糊
image = image.filter(ImageFilter.BLUR)
image.save('img/code.jpg', 'jpeg')
print('end生成验证码图片')

#更多PIL的强大功能，参考Pillow官方文档：https://pillow.readthedocs.org/