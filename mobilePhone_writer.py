#data = {"_key":"2147283","_id":"mobilePhone/2147283","_rev":"_YjgNk0u--_","value":13804562715,"link_type":204}
import random
import time
from  multiprocessing import Process,Pool
import json
import codecs

#随机生成手机号码
def createPhone():
    for k in range(10):
        prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188", "189"]
        return int(random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8)))

def writer_file():

    for i in range(100):

        finall = {"_key":str(i+1),"_id":"mobilePhone/" + str(i+1),"value":createPhone(),"link_type":204}
        # finall ={"_key": str(i), "_id": "mobilePhone/" + str(i),"value":addr(), "link_type": 202,"type": [221]}
        json_str = json.dumps(finall, ensure_ascii=False)
        print(json_str)
        with codecs.open(r'F:\TEST2\mobilePhone.jsonl', 'a',
                         encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
            f.write(json_str)
            f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

writer_file()