#data = {"_key":"2773120","_id":"mobilePhoneR/2773120","_from":"customNum/1969513","_to":"mobilePhone/2147283","_rev":"_Ytg-Owe--_","relation":"拥有","link_type":24,"weight":0.7}
import json
import codecs
import random

def w_code():

    for i in range(1,101):
        ID = "mobilePhoneR/" + str(i)
        # key = i
        from_c = "customNum/" + str(i)
        some = random.sample(range(1, 101), 2)
        if i not in some:
            b = ["mobilePhone/" + str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                # data = {"_id":ID, "_from": from_c, "_to": body,"relation": [221], "link_type": 22, "weight": 0.3}
                data = {"_id":ID,"_from":from_c,"_to":body,"relation":"拥有","link_type":24,"weight":0.7}
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST2\mobilePhoneR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()