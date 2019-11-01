#data = {"_key":"7663610","_id":"AddrR/7663610","_from":"customNum/1977098","_to":"Addr/7528880","_rev":"_YueeQca--_","relation":[221],"link_type":22,"weight":0.3}
import json
import codecs
import random

def w_code():

    for i in range(0,1000):
        ID = "AddrR/" + str(i+1)
        # key = i
        from_c = "customNum/" + str(i+1)
        some = random.sample(range(1, 1000), 2)
        if i not in some:
            b = ["Addr/" + str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                data = {"_id":ID, "_from": from_c, "_to": body,"relation": [221], "link_type": 22, "weight": 0.3}
                # data = {"_id":ID,"_from":from_c,"_to":body,"relation":"属于","link_type":21,"weight":0.2}
                json_str = json.dumps(data, ensure_ascii=False,sort_keys=True)
                print(json_str)
                with codecs.open(r'F:\TEST3\AddrR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()


