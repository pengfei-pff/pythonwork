#data = {"_key":"2963203","_id":"NodeIP/2963203","_rev":"_YjgOUYW--B","value":"61.0.0.210","link_type":401}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs

#随机生成ip地址

def get_random_ip():
    IP1 = random.randint(1,255)
    IP2 = random.randint(1,255)

    abc = '%s.%s.%s.%s.%s.%s' % (IP1, IP2, "1.1",IP1, IP2, "255")
    return abc

def writer_file():

    for i in range(100):

        finall = {"_key":str(i+1),"_id":"NodeIP/" + str(i+1),"value":get_random_ip(),"link_type":401}
        # data = {"_key":"2963203","_id":"NodeIP/2963203","value":"61.0.0.210","link_type":401}
        json_str = json.dumps(finall, ensure_ascii=False)
        print(json_str)
        with codecs.open(r'F:\TEST2\NodeIP.jsonl', 'a',
                         encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
            f.write(json_str)
            f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

writer_file()