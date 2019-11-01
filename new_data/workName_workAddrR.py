#data = {"_key":"7713684","_id":"workName_workAddrR/7713684","_from":"workName/7518928","_to":"Addr/7528956","_rev":"_Yt0RL9a--_","relation":[226],"link_type":22,"weight":0.5}
import json
import codecs
import random

def w_code():

    for i in range(1,100):
        ID = "workName_workAddrR/" + str(i)
        # key = i
        from_c = "workName/" + str(i)
        some = random.sample(range(1, 100), 2)
        if i not in some:
            b = ["Addr/" + str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                # data = {"_id":"workName_workAddrR/7713684","_from":"workName/7518928","_to":"Addr/7528956","relation":[226],"link_type":22,"weight":0.5}
                data = {"_from":from_c,"_to":body,"relation":[226],"link_type":22,"weight":0.5}
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST2\workName_workAddrR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()