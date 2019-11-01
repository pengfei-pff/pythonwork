import unittest
from ddt import ddt,data
from test_faker.do_excel import DoExcel
from test_faker.do_mysql import MySql

test_data = res_data = DoExcel().get_data('data.xlsx','faker_data')

@ddt
class TestMath(unittest.TestCase):
    @data(*test_data)
    def test_add(self,item):
        if item['data'].find('${loan_id}')!= -1:
            if getattr(GetData,'loan_id')==None:
                sql = 'select max(id) from loan where numberid ={0}'.format(getattr(GetData,loan_number))
                loan_id = MySql().do_mysql(sql)
                item['data'] = item['data'].replace('${loan_id}',str(loan_id))
                setattr(GetData,'load_id',loan_id) #利用反射存储结果
            else:
                item['data'] = item['data'].replace('${loan_id}',str(getattr(GetData,'loan_id')))

        res = HttpRequest.http_request(item['url'],eval(item['data'],item['http_method']))
        if res.cookies:
            setattr(GetCookie,'Cookie',res.cookies)
        try:
            self.assertEqual(str(item['excepted']),res.json()['code'])
            TestResult = 'PASS' #成功
        except AssertionError as e:
            TestResult = 'Failed'#失败
            print('执行用例错误：{}'.format(e))
            raise e
        finally:
            DoExcel().write_data(test_case_path,'login',item['case_id']+1,str(res.json()))
            print('获取的结果是：{}'.format(res.json()))

if __name__ == '__main__':
    unittest.main()
