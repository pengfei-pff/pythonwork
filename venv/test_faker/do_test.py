# from test_faker.do_excel import DoExcel
# res_data = DoExcel.get_data('data.xlsx')
# import pandas as pd
# df = pd.read_excel('data.xlsx',sheet_name = 'state_data')
# #获取最大行，最大列
# nrows=df.shape[0]
# ncols=df.columns.size
# print("=========================================================================")
# print('Max Rows:'+str(nrows))
# print('Max Columns'+str(ncols))
# data =(df.ix[0].values)[0]
# print(data)

# from test_faker.get_data import GetData
# item = {'company': '${loan_id}', 'idCard': '350481196006057647', 'phone_number': '18612810759', 'name': '谢萍', 'c_id': 3210, 'address': '天津市倩县西峰杨街M座 673423'}
# # print(item['company'])
# if item['company'].find('${loan_id}')!= -1:
#     item['company'] = item['company'].replace('${loan_id}',GetData.loan_id)
# print(item)

# import mysql.connector
# class DoMysql:
#     def do_mysql(self,cid):
#         config = {'host':"127.0.0.1",
#                   'user':"root",
#                   'password':'123456',
#                   'port':'3306',
#                   'database':'test'}
#         #创建数据库的连接
#         cnn = mysql.connector.connect(**config)
#         #创建游标
#         cursor = cnn.cursor()
#         #编写sql语句
#         sql = 'select * from ceshi where cid ={0}'.format(cid)
#         #执行测试语句
#         cursor.execute(sql)
#         #获取执行结果
#         res = cursor.fetchone()
#         print(res)
#         #关闭游标
#         cursor.close()
#         cnn.close()
#
# if __name__ == '__main__':
#     DoMysql().do_mysql('13945038333')

# _*_ coding:utf-8 _*_
import random
qiu=[]
while True:
  hong = random.randint(1,33)#产生一个随机红球
  if hong in qiu:
    continue#跳过本次循环
  qiu.append(hong)#把红色号码添加到列表
  if len(qiu)==6:
    break
qiu.sort()
lan=random.randint(1,16)#产生一个随机篮球
s=""
for i in qiu:
  s=s+"%02d " %i#02d表示是2位数的整数，个数自动补0
print("预测结果：")
print(s+"+ "+"%02d" %lan)

