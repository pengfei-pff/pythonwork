#data = {"_key":"2964843","_id":"MachineNum/2964843","_rev":"_YjgOAkm--_","value":"X562-27807","link_type":301}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs

#随机设备号
def value():
    for k in range(4):
        prelist = "X562-"
        return prelist+ "".join(random.choice("0123456789") for i in range(9))

def writer_file():

    for i in range(100):

        finall = {"_key":str(i+1),"_id":"MachineNum/" + str(i+1),"value":value(),"link_type":301}
        # data = {"_key":"2964843","_id":"MachineNum/2964843","value":"X562-27807","link_type":301}
        json_str = json.dumps(finall, ensure_ascii=False)
        print(json_str)
        with codecs.open(r'F:\TEST2\MachineNum.jsonl', 'a',
                         encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
            f.write(json_str)
            f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

writer_file()