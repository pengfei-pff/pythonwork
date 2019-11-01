#data = {"_key":"7613612","_id":"workNameR/7613612","_from":"customNum/1977098","_to":"workName/7518849","_rev":"_Ytg_MB6--_","link_type":25,"relation":"就职","weight":0.2}
import json
import codecs
import random

def w_code():

    for i in range(1,101):
        ID = "customNum/"+str(i)
        # key = i
        # from_c = "customNum/" + str(i)
        some = random.sample(range(1, 100), 2)
        if i not in some:
            b = [str(c) for c in some]
            # relation = ["朋友", "兄弟", "夫妻", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                b = "workName/" +body
                # data = {"_id":"workNameR/7613612","_from":"customNum/1977098","_to":"workName/7518849","link_type":25,"relation":"就职","weight":0.2}
                data = {"_from":ID,"_to":b,"link_type":25,"relation":"就职","weight":0.2}
                # data = { "source": ID, "target": int(body), "relation": m, "value": 3 }
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST2\workNameR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()