# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#Base64
#准备一个包含64个字符的数组 ['A', 'B', 'C',...'a', 'b', 'c',...'0', '1',...'+', '/']
#对二进制数据进行处理，每3个字节一组，一共是3*8=24bit，划分4组，每组正好6个bit
#这样得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串

#所以Base64编码会把3个字节的二进制数据编码为4个字节的文本数据，长度增加33%，好处是编码后文本数据可以在邮件正文，网页等直接显示。
#如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

#python内置的base64可以直接进行base64的编解码
import base64
ec = base64.b64encode(b'binary\x00string')
print(ec) # b'YmluYXJ5AHN0cmluZw=='
dc = base64.b64decode(ec)
print(dc)

#由于标准的Base64编码后可能会出现字符+和/，在URL中就不能直接作为参数，所以又有一种‘url safe’的base64编码，其实就是把字符+和/分别变成-和_
b = b'i\xb7\x1d\xfb\xef\xff'
print('base64 encode', b, ':', base64.b64encode(b))
print('base64 urlsafe encode', b, ':', base64.urlsafe_b64encode(b))
print('base64 urlsafe decode abcd--__ :', base64.urlsafe_b64decode('abcd--__'))

#可以自定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要
#Base64是一种通过查表的编码方法，不能用于加密，即使使用自定的编码表也不行
#Base64适用于小段内容的编码，比如数字证书签名，Cookie的内容等

#由于=字符也可能出现在Base64编码中，但=用在URL,Cookie里面会造成歧义，所以很多Base64编码后会把=去掉
#标准Base64 ： 'abcd' -> 'YWJjZA=='
#自动去掉= ： 'abcd' -> 'YWJjZA' 
#去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

#写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    print(len(s) % 4)
    s = s + b'=' * (4 - len(s) % 4)
    print(base64.b64decode(s))
    return base64.b64decode(s)

#Test
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
assert b'abcd' == safe_base64_decode(b'YWJjZA='), safe_base64_decode('YWJjZA=')
print('Pass')