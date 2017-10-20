# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#python的hashlib提供了常见的摘要算法，如MD5,SHA1等等
#摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#如果数据量很大，可以分块多次调用update(),最后计算的结果是一样的
md52 = hashlib.md5()
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))
print(md52.hexdigest())
#MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，通常用一个32位的16进制字符串表示

#另一种摘要算法是SHA1,调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
#SHA1的结果是160bit字节，通常用一个40位的16进制字符串表示
#比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

#练习 根据用户输入的口令，计算出存储在数据库中的MD5口令
def calc_md5(password):
    word = hashlib.md5()
    word.update(password.encode('utf-8'))
    sqlWord = word.hexdigest()
    print(sqlWord)
    return sqlWord

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',#123456
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    sqlWord = calc_md5(password)
    if (db[user] == sqlWord):
        print('login success')
    else:
        print('login fail')
login('michael', '123456')

#加盐
def calc_md5_salt(password):
    return calc_md5(password + 'the-Salt')

#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
from collections import defaultdict
db = defaultdict(lambda: '')

def register(username, password):
    if db[username]:
        print(username, 'alreay exist! please change another name')
        return False
    db[username] = calc_md5(password + username + 'the-Salt')
    print('register success')
    return True

def loginUser(username, password):
    if db[username]:
        if db[username] == calc_md5(password + username + 'the-Salt'):
            print('login success')
            return True
        else:
            print('login fail --  password error')
            return False
    print('login fail -- name', username, 'has not register')
    return False

continueProcess = True
while continueProcess:
    num = input('please input 1 for register, 2 for login, 3 for exit, 4 for db :')
    try:
        num = int(num)
        if num == 1:
            #register
            username1 = input('please input username for register:')
            password1 =  input('please input password for register:')
            register(username1, password1)
        elif num == 2:
            #login
            username2 = input('please input username for login:')
            password2 =  input('please input password for login:')
            loginUser(username2, password2)
        elif num == 3:
            continueProcess = False
        elif num == 4:
            print(db)
        else:
            print('input number error')
    except:
        print('please input a number:1,2,3')


