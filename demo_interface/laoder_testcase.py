from demo_interface.unittest_new import TestInterface
import unittest
import HTMLTestRunner
from demo_interface.unittest_new import TestInterface
from test_faker.do_excel import DoExcel
test_data = DoExcel('test.xlsx','test').get_data()
suite = unittest.TestSuite()
# loader = unittest.TestLoader()   #创建loader装载器
# test_case = loader.loadTestsFromTestCase(TestInterface) #调用loader装载器的loadTestsFromTestCase方法
for item in test_data:
    suite.addTest(TestInterface(eval(item['url']),eval(item['data']),eval(item['method']),eval(item['excepted'])))
#采用上下文管理器，不用每次手动关闭文件
with open('test_report.html','wb')as file:
    #执行测试用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=2,title='test001',description='first one test') #verbosity=2显示测试用例最详细的信息，使用stream
    runner.run(suite)



