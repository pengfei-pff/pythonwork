#data = {"_key":"2136368","_id":"phone/2136368","_rev":"_YjgNaU----","value":213915915844,"link_type":203}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs
import csv

#随机生成电话
def createPhone():
    for k in range(10):
        prelist=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        return int(random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8)))

def writer_file():
    csvFile = open(r"F:\TEST3\phone.csv", "w", newline="")  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow(["name:ID(NodeIP-ID)", "data", "link_type", ":LABEL"])  # 写入列的名称
    for i in range(100):
        writer.writerow([(str(i+1)), createPhone(), 203, "phone"])
    csvFile.close()


writer_file()