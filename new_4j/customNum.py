import csv
import random
import time
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
    csvFile = open("F:\TEST3\customNum.csv", "w", newline="",encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow(["name:ID(customNum-ID)", "data", "createDate", "link_type",":LABEL"])  # 写入列的名称
    # 写入多行用writerows                                #写入多行
    for i in range(400):
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        t = random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        # print(date)
        writer.writerow([( str(i+1)),v_code(),date,101,"customNum"])
    csvFile.close()
        # finall ={"_key": str(i+1), "_id": "customNum/" + str(i+1),"value":v_code(), "createDate": date, "link_type": 101}
        # json_str = json.dumps(finall, ensure_ascii=False)
        # print(json_str)
        # with codecs.open(r'F:\TEST3\customNum.jsonl', 'a',
        #                  encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
        #     f.write(json_str)
        #     f.write('\n')  # 如果循环写入多个json数据需要加一个换行符
writer_file()