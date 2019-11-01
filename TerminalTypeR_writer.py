#data = {"_key":"8028271","_id":"TerminalTypeR/8028271","_from":"TerminalType/2993469","_to":"MachineNum/2964843","_rev":"_YtgBoR6--_","relation":"属于","link_type":42,"weight":0.25}
import json
import codecs
import random

def w_code():

    for i in range(1,100,2):
        ID = "TerminalTypeR/" + str(i)
        key = [2993469,2993470,2993471]
        m = random.randint(0,2)
        from_c = "TerminalType/" +str(key[m])
        to_c = "MachineNum/" + str(random.randint(1,100))

        # data = {"_id":"TerminalTypeR/8028271","_from":"TerminalType/2993469","_to":"MachineNum/2964843","relation":"属于","link_type":42,"weight":0.25}
        data = {"_id":ID,"_from":from_c,"_to":to_c,"relation":"属于","link_type":42,"weight":0.25}
        json_str = json.dumps(data, ensure_ascii=False)
        print(json_str)
        with codecs.open(r'F:\TEST2\TerminalTypeR.jsonl', 'a',
                         encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
            f.write(json_str)
            f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()