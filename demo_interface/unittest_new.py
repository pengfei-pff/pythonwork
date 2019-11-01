import unittest
from demo_interface.http_requests import HttpMain
from demo_interface.get_cookie import GetData

class TestInterface(unittest.TestCase):
    def setUp(self):
        pass
    def __init__(self,methodName,url,data,method,expected):
        super(TestInterface,self).__init__(methodName)#使用超继承，继承父类的__init__方法
        self.url = url
        self.data = data
        self.method = method
        self.expected =expected
    def test_api(self):#一个用例一个函数，不能传参
        result = HttpMain().run_main(self.url,self.method,self.data,getattr(GetData,'cookie'))
        if result.cookies:
            setattr(GetData,'Cookie',result.cookies)
        try:
            self.assertEqual(self.expected,result.json()['status'])
        except Exception as e:
            print('错误信息{}'.format(e))
            raise e
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()     #主要用于测试，测试用例的执行顺序根据测试用例集的名字排序，test_1>>test_2
