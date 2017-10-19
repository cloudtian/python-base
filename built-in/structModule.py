# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#struct模块来解决bytes和其他二进制数据类型的转换

#struct的pack函数把任意数据类型变成bytes
import struct
print(struct.pack('>I', 10240099))
#pack的第一个参数是处理指令，'>I'的意思是：
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
#后面的参数格式要和处理指令一致

#unpack把bytes变成相应的数据类型
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
#根据>IH的说明，后面的bytes依次变为I:4字节无符号整数和H:2字节无符号整数

#尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了

#struct模块定义的数据类型可以参考Python官方文档：https://docs.python.org/3/library/struct.html#format-characters

#BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

#两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
#一个4字节整数：表示位图大小；
#一个4字节整数：保留位，始终为0；
#一个4字节整数：实际图像的偏移量；
#一个4字节整数：Header的字节数；
#一个4字节整数：图像宽度；
#一个4字节整数：图像高度；
#一个2字节整数：始终为1；
#一个2字节整数：颜色数。

#读入前30个字节来分析
#s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
#struct.unpack('<ccIIIIIIHH', s)
#(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
#结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。

#练习
#bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数