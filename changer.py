import pandas as pd
import os
'''修改文件，某一列的格式'''
def change_ralation():
    data = pd.read_csv(r'C:\Users\pengfei\Desktop\TEST\2222.csv', encoding='utf-8', )
    data[u"relationship"] = data[u"relationship"]

    print(data[u"relationship"])
    # data[u"relationship"] = data[u"relationship"].apply(lambda x: x.eval())
    data.to_csv(r'C:\Users\pengfei\Desktop\TEST\2222.csv', index=False, encoding='utf-8')


change_ralation()

