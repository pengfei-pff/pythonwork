#data = {"_key":"7613612","_id":"workNameR/7613612","_from":"customNum/1977098","_to":"workName/7518849","_rev":"_Ytg_MB6--_","link_type":25,"relation":"就职","weight":0.2}
import json
import codecs
import random
import csv

def w_code():
    csvFile = open(r"F:\TEST3\workNameR.csv", "w", newline="", encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow([":START_ID(customNum-ID)", ":END_ID(Addr-ID)", "link_type", "relation", "weight", ":TYPE"])  # 写入列的名称
    for i in range(1,400,2):
        ID = str(i)
        # key = i
        # from_c = "customNum/" + str(i)
        some = random.sample(range(1, 100), 1)
        if i not in some:
            b = [str(c) for c in some]
            # relation = ["朋友", "兄弟", "夫妻", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                writer.writerow([ID, body,25,"就职", 0.2, "workNameR"])
    csvFile.close()


w_code()