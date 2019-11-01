import csv
import random
import time
from  multiprocessing import Process,Pool

a1=(1976,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(1990,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

def v_code():
    ret = ""
    for i in range(25):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter = chr(random.randint(97, 122))#取小写字母
        Letter = chr(random.randint(65, 90))#取大写字母
        s = str(random.choice([num,letter,Letter]))
        ret += s
    return ret
# def w_code(a,some):
#     '''第一个写完文件，第二个文件实现读取第一个文件生成另一个文件'''
#
#     csvFile = open(r"C:\Users\pengfei\Desktop\TEST\1111.csv","w",newline="")            #创建csv文件写customNum表
#     writer = csv.writer(csvFile)                  #创建写的对象
#     #先写入columns_name
#     writer.writerow(["from","to","relationship"])     #写入列的名称
#     #写入多行用writerows                                #写入多行
#
#     for i in range(10000000):  #测试环节数据
#     #     # print(date)
#         relation = ["家人","兄弟","子女","母子","父母","父子","父女","母女"]
#         n = random.randint(1, 3)
#         writer.writerow([a,some,random.sample(relation,n)])
#         csvFile.close()
# # print(v_code())




def writer_file():
    csvFile = open(r"C:\Users\pengfei\Desktop\TEST\2222.csv","w",newline="")            #创建csv文件写customNum表
    writer = csv.writer(csvFile)                  #创建写的对象
    #先写入columns_name
    writer.writerow(["value","createDate","_key"])     #写入列的名称
    #写入多行用writerows                                #写入多行
    list = []
    for i in range(10):

        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        t = random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        # print(date)
        fvm = random.randint(100000, 999999)
        list2 = list.append(fvm)
        writer.writerow([v_code(),date,fvm])
    csvFile.close()
    # print(list)
    '''随机取列表中的数值'''
    for customNum in list:
        a = customNum
        some = random.sample(list, 3)
        # print(a)
        # if a != b and a != c and a != d:
        # if a not in some:
        w_code(a,some)


if __name__ == '__main__':
    start_time = time.time()
    pool = Pool()
    for i in range(10):
        pool.apply_async(func=writer_file,)
        # pool.apply(func=Foo, args=(i,))
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    end_time = time.time()
    print('消耗时长',start_time-end_time)



