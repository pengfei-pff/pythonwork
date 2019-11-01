#data = {"_key":"2964843","_id":"MachineNum/2964843","_rev":"_YjgOAkm--_","value":"X562-27807","link_type":301}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs
import csv

#随机设备号
def value():
    for k in range(4):
        prelist = "X562-"
        return prelist+ "".join(random.choice("0123456789") for i in range(9))

def writer_file():
    csvFile = open("F:\TEST3\MachineNum.csv", "w", newline="")  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow(["name:ID(Addr-ID)","data","link_type",":LABEL"])  # 写入列的名称
    for i in range(100):
        writer.writerow([(str(i + 1)),value(),301,"MachineNum"])
    csvFile.close()


writer_file()