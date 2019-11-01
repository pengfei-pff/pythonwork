import os
path0 = os.path.realpath(__file__) #获取当前路径
path1 = os.path.split(os.path.realpath(__file__))[0] #将路径进行分割，获取上一级路径
path2 = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


#测试用例的路径
test_case = os.path.join(path1,'test_data','test_data.xlsx') #将路径进行拼接
print(path0)
print(path1)
print(path2)
print(test_case)
