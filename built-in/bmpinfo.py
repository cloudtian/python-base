# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数

import struct

def checkBMP(fileAddr):
    try:
        with open(fileAddr, 'rb') as f:
            file30b = f.read(30) #读取前30个字节来分析
        result = list(struct.unpack('<ccIIIIIIHH', file30b))
        if result[0] == b'B' and (result[1] == b'M' or result[1] == b'A'):
            print('This file is a bmp format:', result)
            print('size:', result[6], ' *', result[7])
            print('color number:', result[9])
        else:
            print('This file is not a bmp format')
    except:
        print('file error, please check if file exist')

if __name__ == '__main__':
    addr = input('input file address:')
    checkBMP(addr)