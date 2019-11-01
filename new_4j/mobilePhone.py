#data = {"_key":"2147283","_id":"mobilePhone/2147283","_rev":"_YjgNk0u--_","value":13804562715,"link_type":204}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs
import csv

#随机生成手机号码
def createPhone():
    for k in range(10):
        prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188", "189"]
        return int(random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8)))

def writer_file():
    csvFile = open("F:\TEST3\mobilePhone.csv", "w", newline="")  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow(["name:ID(mobilePhone-ID)", "data", "link_type", ":LABEL"])  # 写入列的名称
    for i in range(100):
        writer.writerow([(str(i + 1)), createPhone(), 204, "mobilePhone"])
    csvFile.close()


writer_file()