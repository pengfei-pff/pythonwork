from test_faker.do_excel import DoExcel
from faker import Faker
'''
生成测试各种测试数据写入excel中用于取值使用
'''
faker = Faker('zh_CN')#实例化faker,将faker数据写入excel中

for item in range(1,10001):
    name = faker.name()
    phone_number = faker.phone_number()
    address = faker.address()
    company = faker.company()
    idCard = faker.ssn()
    time = faker.date_time()
    DoExcel().write_data('data.xlsx','faker_data',item,name,phone_number,idCard,company,address)
    print('生成测试数据--{0},{1}'.format(item,name))

# fileContent = '姓名:%s'%name,'   身份证:%s'%idCard,'   手机号:%s'%phone_number,'   公司:%s'%company,'   地址:%s'%address
