import pandas as pd
df = pd.read_excel('data.xlsx',sheet_name = 'state_data')

class GetData:
    cookie = '小郭'
    load_id =None
    loan_number = None
    loan_id = data =(df.ix[0].values)[0]

# print(GetData.cookie) #获取内部属性
# setattr(GetData,'cookie','小黄')#修改内部属性值
# print(hasattr(GetData,'cookie'))#判断是否有这个属性值
# print(GetData.cookie)
# print(GetData.loan_id)