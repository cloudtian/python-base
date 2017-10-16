# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#常用内建模块：datetime,collections,base64,struct,hashlib,itertools,contextlib,XML,HTMLParser,urllib

#datetime是python处理日期和时间的标准库
from datetime import datetime 
#datetime是模块，datetime模块包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
#如果仅import datetime，则必须引用全名datetime.datetime
now = datetime.now() #获取当前datetime
print('获取当前datetime', now)
print(type(now))

dt = datetime(2017, 10, 16, 16, 48) #用指定日期时间创建datetime
print(dt)

#datetime转换为timestamp, 秒为单位
print('datetime转换为timestamp', dt.timestamp())
#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
#javascript:获取时间戳 Date.now()，以毫秒为单位

t = 1508143680.0
print('本地时间', datetime.fromtimestamp(t)) #本地时间
print('UTC时间', datetime.utcfromtimestamp(t)) #UTC时间

#str转换为datetime
cday = datetime.strptime('2017-10-16 16:57:00', '%Y-%m-%d %H:%M:%S')
print('str转换为datetime', cday) #转换后的datetime是没有时区信息的
#字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式 https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

#datetime转换为str
now = datetime.now()
print(now)
print('datetime转换为str', now.strftime('%a, %b %d %H:%M'))

#datetime加减，对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime;加减可以直接用+和-运算符，不过要导入timedelta这个类
from datetime import timedelta
now = datetime.now()
print(now)
print('now+10hours:', now + timedelta(hours=10))
print('now-1day:', now - timedelta(days=10))
print('now+2days12hours:', now + timedelta(days=2, hours=12))

#本地时间转换为UTC时间，本地时间是只系统设定时区的时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) #创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) #强制设置为UTC+8:00
print('本地时间转换为UTC时间', dt) #如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

#时区转换，可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
#拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc时间', utc_dt)
#astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt', bj_dt)
#astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt', tokyo_dt)
#astimezone()将bj_dt转换时区为东京时间
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt', tokyo_dt)

#时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间
#利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
#注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

#小结
#datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

#练习
dt = '2015-1-21 9:01:30'
tz = 'UTC+5:00'
import re
def to_timestamp(dt_str, tz_str):
    #将dt_str转换为datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    #根据tz_str获取时区信息
    tz = re.match(r'^UTC([+|-]\d+):\d+$', tz_str).group(1)
    #强制设置时区
    dt_tz = dt.replace(tzinfo=timezone(timedelta(hours=int(tz))))
    dt_tz_ts = dt_tz.timestamp()
    print(dt_str, tz_str, '转换成时间戳:', dt_tz_ts)
    return dt_tz_ts

t1= to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('pass')