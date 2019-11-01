#data = {"_key":"7713684","_id":"workName_workAddrR/7713684","_from":"workName/7518928","_to":"Addr/7528956","_rev":"_Yt0RL9a--_","relation":[226],"link_type":22,"weight":0.5}
import json
import codecs
import random
import csv

def w_code():
    csvFile = open(r"F:\TEST3\workName_workAddrR.csv", "w", newline="", encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow([":START_ID(workName-ID)", ":END_ID(Addr-ID)", "relation", "link_type", "weight", ":TYPE"])  # 写入列的名称
    for i in range(1,100):
        ID = "workName_workAddrR/" + str(i)
        # key = i
        from_c = str(i)
        some = random.sample(range(1, 100), 2)
        if i not in some:
            b = [ str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                writer.writerow([from_c, body, [226], 22,0.5, "workName_workAddrR"])
    csvFile.close()

w_code()