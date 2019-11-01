import cx_Oracle
import time
import random
from test_faker.do_excel import DoExcel
from faker import Faker
'''
使用生成的测试数据进行oracal数据插入，形成有关系的网络数据
'''
data_faker = DoExcel().get_data('data.xlsx', 'faker_data')  # 将excel的数据传入列表中用于随机取值使用

class IdCard:
    def id_data(self):
        random_num = random.randint(1,100)
        data_cid =[]
        for item in data_faker:
            data_cid.append(item['idCard'])
        return data_cid[random_num]
class  Name:
    def name_data(self):
        random_num = random.randint(1, 100)
        data_cname =[]
        for item in data_faker:
            data_cname.append(item['name'])
        return data_cname[random_num]
class AddRess:
    def address_data(self):
        random_num = random.randint(1, 100)
        data_address =[]
        for item in data_faker:
            data_address.append(item['address'])
        return data_address[random_num]

class DoOracal:
    def create_data(self,create_num):
        sum = 0
        for i in range(create_num):
            try:
                db = cx_Oracle.connect('klg/klg@10.111.32.24/orcl')
                cr = db.cursor()
            except exception as e:
                print('database connection fail，error{0}'.format(e))

            data_faker = DoExcel().get_data('data.xlsx', 'faker_data')  # 将excel的数据传入列表中用于随机取值使用

            faker = Faker('zh_CN') #实例化faker

            idCard = IdCard().id_data()
            address = AddRess().address_data()
            # address = '北京市东三环浪人街区'
            name = Name().name_data()
            phone_number = '17611158745'
            company = '北京市哈哈哈有限公司'

            print('姓名--{0},身份证--{1}，手机号--{2}，地址--{3}，公司--{4}'.format(name, idCard, phone_number, address, company))
            time_time = faker.date_time(tzinfo=None)  # 随机日期时间
            print(time_time) #打印随机生成的日期
            print(name,idCard,phone_number)#打印随机生成的信息
            sum = sum + 1
            sql = "insert into t_app_demo"+\
                  "(APP_PROFILE_SEQ, PKEY, APP_DEMO_CUSTNO, APP_DEMO_NAME, APP_DEMO_IDTYPE, APP_DEMO_ID, APP_DEMO_GENDER, APP_DEMO_BIRTH, APP_DEMO_MARRY, APP_DEMO_COMP, APP_DEMO_PHONE, APP_DEMO_WKNO, APP_DEMO_HOMENO, APP_DEMO_EDUCATION, APP_DEMO_HOUSEHOLD, APP_DEMO_CONTACT, APP_DEMO_HOMEADD, APP_DEMO_WORKADD, APP_DEMO_EMAIL, APP_DEMO_INDUS, APP_DEMO_LOCALYRS, APP_DEMO_HOUSEST, SYS_DATE)"+\
                  "values ('NPL" + str(sum) + "', 'KLD"+str(sum)+"', 'LK500021781', '" + name + "', '身份证', '"+idCard+"', '男', to_date('09-08-1992', 'dd-mm-yyyy'), '已婚', '网易', " + phone_number + ", '67895432', '65557888', '硕士', '北京', '北京朝阳', '"+address+"', '网易科技股份公司', 'xuqing@wangyi.com', 'IT', 1, '有房屋', to_date('19-08-2019', 'dd-mm-yyyy'))"
            cr.execute(sql)
            print('Table is ok')
            cr.close()
            db.commit()
            db.close()

if __name__ == '__main__':
    DoOracal().create_data(10)

# data_faker = DoExcel().get_data('data.xlsx', 'faker_data')  # 将excel的数据传入列表中用于随机取值使用








