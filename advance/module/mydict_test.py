import unittest

from mydict import Dict

class TestDict(unittest.TestCase):#编写测试类，继承unittest.TestCase

    #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1) #断言d.a与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        print('test_init...')
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        print('test_key...')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        print('test_attr...')
    
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): #期待抛出指定类型的错误
            value = d['empty']
        print('test_keyerror...')
        
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
        print('test_attrerror...')

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()