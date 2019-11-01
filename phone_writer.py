#data = {"_key":"2136368","_id":"phone/2136368","_rev":"_YjgNaU----","value":213915915844,"link_type":203}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs

#随机生成电话
def createPhone():
    for k in range(10):
        prelist=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        return int(random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8)))

def writer_file():

    for i in range(100):

        finall ={"_key":str(i+1),"_id":"phone/" + str(i+1),"value":createPhone(),"link_type":203}
        # finall ={"_key":str(i),"_id":"phone/" + str(i),"value":createPhone()"link_type":204}
        json_str = json.dumps(finall, ensure_ascii=False)
        print(json_str)
        with codecs.open(r'F:\TEST2\phone.jsonl', 'a',
                         encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
            f.write(json_str)
            f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

writer_file()