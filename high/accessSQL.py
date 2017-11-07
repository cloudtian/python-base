# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#数据库的类别：
#付费的商用数据库：Oracle,SQL Server,DB2,Sybase
#免费开源数据库：MySQL,PostgreSQL,sqlite

#要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection
#连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果

#由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库

#导入SQLite驱动
import sqlite3
#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建：
conn = sqlite3.connect('db/test.db')
#创建一个cursor
cursor = conn.cursor()
#执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Cloud\')')
#通过rowcount获得插入的行数
print(cursor.rowcount)
#关闭cursor
cursor.close()
#提交事务
conn.commit()
#关闭connection
conn.close()

#查询记录
conn = sqlite3.connect('db/test.db')
cursor = conn.cursor()
#执行查询语句
cursor.execute('select * from user where id=?', ('1',))
#获得查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

#使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
#使用Cursor对象执行insert,update,delete语句时，执行结果有rowcount返回影响的行数，就可以拿到执行结果。
#使用Cursor对象执行select语句时，通过fetchall()方法可以拿到结果集。结果集是一个list，每个元素都是一个tuple,对应一行记录。
#如果SQL语句带有参数，那么需要把参数按照位置传给execute()方法，有几个?占位符就必须对应几个参数。

#练习，根据分数段查找指定的名字
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'db/test2.db')
if os.path.isfile(db_file):
    os.remove(db_file)
#初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    #返回指定分数区间的名字，按分数从低到高排序
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select name from user where score between ? and ? order by score', (low, high))
    values = cursor.fetchall()
    print(values)
    return list(map(lambda x: x[0], values))
#测试
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)


#SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
#1.安装MySQL：http://dev.mysql.com/downloads/mysql/5.6.html （安装时请选择UTF-8编码，以便正确地处理中文。）
#注：如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。
#2.安装MySQL驱动：pip install mysql-connector-python --allow-external mysql-connector-python  
#如果上面的命令安装失败，可以试试另一个驱动：pip install mysql-connector

#操作MySQL的数据库代码和SQLite类似：执行INSERT等操作后要调用commit()提交事务；MySQL的SQL占位符是%s。

#使用SQLAlchemy:ORM框架 (Object-Relational Mapping)
#安装：pip install sqlalchemy