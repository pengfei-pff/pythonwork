#生成Account_customNumR表测试数据
#data={"_key":"3188943","_id":"Account_customNumR/3188943","_from":"Account/3088861","_to":"customNum/1995990","_rev":"_Ytf945e---","relation":"属于","link_type":21,"weight":0.2}
import json
import codecs
import random

def w_code():

    for i in range(0,100):
        ID = "Account_AddrR/" + str(i+1)
        # key = i
        from_c = "Account/" + str(i+1)
        some = random.sample(range(0, 100), 1)
        if i not in some:
            b = ["Addr/" + str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                # data = {"_id":ID, "_from": from_c,"_to": body, "_rev": "_YtgBRzq--_", "relation": m, "link_type": 11,"weight": 0.9}
                data = {"_from":from_c,"_to":body,"relation":"属于","link_type":66,"weight":0.7}
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST2\Account_AddrR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()