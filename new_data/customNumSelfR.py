import json
import codecs
import random

def w_code():
    sum = 1
    for j in range(1,500):
        for i in range(1,3):
            ID = "customNumSelfR/" + str(i+1)
            # key = i
            from_c = "customNum/" + str(j)
            sum = sum + 1
            relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            m = random.sample(relation, 1)
            data = {"_id":ID, "_from": from_c,
                            "_to": "customNum/" + str(sum), "_rev": "_YtgBRzq--_", "relation": m, "link_type": 11,
                            "weight": 0.9}
            json_str = json.dumps(data, ensure_ascii=False,sort_keys=True)
            print(json_str)
            with codecs.open(r'F:\TEST3\customNumSelfR.jsonl', 'a',encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                f.write(json_str)
                f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()

#data = {"_key":"7663610","_id":"AddrR/7663610","_from":"customNum/1977098","_to":"Addr/7528880","_rev":"_YueeQca--_","relation":[221],"link_type":22,"weight":0.3}
# import json
# import codecs
# import random
#
# def w_code():
#     sum = 1
#     for j in range(1,100):
#         for i in range(1,11):
#             ID = "AddrR/" + str(i+1)
#             from_c = "customNum/" + str(j)
#             sum = sum + 1
#             data = {"_id":ID, "_from": from_c, "_to":"Addr/" + str(sum),"relation": [221], "link_type": 22, "weight": 0.3}
#             json_str = json.dumps(data, ensure_ascii=False,sort_keys=True)
#             print(json_str)
#             with codecs.open(r'F:\TEST3\AddrR.jsonl', 'a',
#                              encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
#                 f.write(json_str)
#                 f.write('\n')  # 如果循环写入多个json数据需要加一个换行符
#
# w_code()