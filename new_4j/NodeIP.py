#-*- coding:utf-8 -*-
#data = {"_key":"2963203","_id":"NodeIP/2963203","_rev":"_YjgOUYW--B","value":"61.0.0.210","link_type":401}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs
import csv
#随机生成ip地址

def get_random_ip():
    IP1 = random.randint(1,255)
    IP2 = random.randint(1,255)

    abc = '%s.%s.%s.%s.%s' % (IP2, "1.1",IP1, IP2, "255")
    return abc

def writer_file():
    csvFile = open(r"F:\TEST3\NodeIP.csv", "w", newline="")  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow(["name:ID(NodeIP-ID)", "data", "link_type", ":LABEL"])  # 写入列的名称
    for i in range(100):
        writer.writerow([(str(i + 1)), get_random_ip(), 401, "NodeIP"])
    csvFile.close()



writer_file()