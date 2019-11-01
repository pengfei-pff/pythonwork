

#data={"_key":"3338984","_id":"Account/3338984","_rev":"_YkIIZLy--_","value":"A8C230C61A737F041A70316CCFF7C8CB","link_type":201}测试数据样例
import csv
import random
import time
import codecs
from  multiprocessing import Process,Pool
import json
import codecs

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

def writer_file():
    csvFile = codecs.open("F:\TEST3\Account.csv", "w",encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow(["name:ID(Account-ID)", "data", "createDate", "link_type", ":LABEL"])  # 写入列的名称
    for i in range(1000):
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        t = random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        # print(date)
        writer.writerow([(str(i + 1)), v_code(), date, 201, "Account"])
    csvFile.close()

writer_file()