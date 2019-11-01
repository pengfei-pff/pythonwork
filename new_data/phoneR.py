#data= {"_key":"2745507","_id":"phoneR/2745507","_from":"customNum/1969513","_to":"phone/2136368","_rev":"_Ytg-dWa--_","relation":"拥有","link_type":23,"weight":0.6}
import json
import codecs
import random

def w_code():

    for i in range(1,1000,5):
        ID = "phoneR/" + str(i)
        # key = i
        from_c = "customNum/" + str(i)
        some = random.sample(range(1, 101), 2)
        if i not in some:
            b = ["phone/" + str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                # data = {"_id":"phoneR/2745507","_from":"customNum/1969513","_to":"phone/2136368","relation":"拥有","link_type":23,"weight":0.6}
                data = {"_id":ID,"_from":from_c,"_to":body,"relation":"拥有","link_type":23,"weight":0.6}
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST3\phoneR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()