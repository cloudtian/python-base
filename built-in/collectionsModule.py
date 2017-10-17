# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#collections是Python内建的一个集合模块

#namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('p.x:', p.x)
print('p.y:', p.y)
#namedtuple是一个函数，用来创建一个自定义的tuple对象，并规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
#namedtuple('名称', [属性list])
Circle = namedtuple('Circle', ['x', 'y', 'r'])

#deque 高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print('deque q:', q)
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素了

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('key1存在，dd[key1]:', dd['key1'])
print('key2不存在，dd[key2]:', dd['key2'])
#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的

#OrderedDict
#使用dict时，Key是无序的，在对dict做迭代时，无法确定Key的顺序，可以使用OrderedDict来保持Key的顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print('d:', d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('od:', od)

#OrderedDict的key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print('key:', od.keys())
print('list key:', list(od.keys()))

#OrderedDict可以实现一个FIFO(先进先出)的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

luod =LastUpdatedOrderedDict(2)
luod['a'] = 1
luod['b'] = 2
luod['c'] = 3
luod['c'] = 4
luod['d'] = 5

#Counter,一个简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print('Counter c:', c) #Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
#Counter实际上是dict的一个子类，从上面结果可以看出，字符'g','m','r'各出现了两次，其他字符各出现了一次
