#data= {"_key":"2745507","_id":"phoneR/2745507","_from":"customNum/1969513","_to":"phone/2136368","_rev":"_Ytg-dWa--_","relation":"拥有","link_type":23,"weight":0.6}
import json
import codecs
import random
import csv

def w_code():
    csvFile = open(r"F:\TEST3\phoneR.csv", "w", newline="", encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow([":START_ID(customNum-ID)", ":END_ID(phone-ID)", "relation", "link_type", "weight", ":TYPE"])  # 写入列的名称
    for i in range(1,101):
        ID = "phoneR/" + str(i)
        # key = i
        from_c = str(i)
        some = random.sample(range(1, 101), 2)
        if i not in some:
            b = [ str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                writer.writerow([from_c, body, "拥有",23,0.6,"phoneR"])
    csvFile.close()


w_code()