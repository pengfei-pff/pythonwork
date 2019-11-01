#data ={"_key":"3043586","_id":"mobilePhone_machineNumR/3043586","_from":"mobilePhone/2149319","_to":"MachineNum/2964843","_rev":"_YtgBdi---_","relation":"申请注册","link_type":33,"weight":0.3}
import json
import codecs
import random

def w_code():

    for i in range(1,100,2):
        ID = "mobilePhone_machineNumR/" + str(i)
        # key = i
        from_c = "mobilePhone/" + str(i)
        some = random.sample(range(1, 101), 1)
        if i not in some:
            b = ["MachineNum/" + str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                data = {"_from":from_c,"_to":body,"relation":"申请注册","link_type":33,"weight":0.3}
                # data = {"_id":ID,"_from":from_c,"_to":body,"relation":"拥有","link_type":24,"weight":0.7}
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST3\mobilePhone_machineNumR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()