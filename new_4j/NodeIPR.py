#data = {"_key":"2993582","_id":"NodeIPR/2993582","_from":"MachineNum/2964843","_to":"NodeIP/2963203","_rev":"_YtgBG4i--_","relation":"位于","link_type":41,"weight":0.7}
import json
import codecs
import random
import csv

def w_code():
    csvFile = open(r"F:\TEST3\NodeIPR.csv", "w", newline="", encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow( [":START_ID(MachineNum-ID)", ":END_ID(NodeIP-ID)", "relation", "link_type", "weight", ":TYPE"])  # 写入列的名称
    for i in range(1,101):
        ID = "NodeIPR/" + str(i)
        # key = i
        from_c =  str(i)
        some = random.sample(range(1, 101), 1)
        if i not in some:
            b = [ str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                writer.writerow([from_c, body, "位于", 41, 0.7, "NodeIPR"])
    csvFile.close()


w_code()