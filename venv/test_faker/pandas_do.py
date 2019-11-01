import pandas as pd

df = pd.read_excel('data.xlsx',sheet_name = 'state_data')
test_data=[]
for i in df.index.values:#获取行号的索引，并对其进行遍历：
    #根据i来获取每一行指定的数据 并利用to_dict转成字典
    row_data=df.ix[i,['李晨','18633804015','652824199902141442','易动力科技有限公司','上海市合山市清城广州街l座 455128',1]].to_dict()
    test_data.append(row_data)
print("最终获取到的数据是：{0}".format(test_data))