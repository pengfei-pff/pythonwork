#data ={"_key":"3043586","_id":"mobilePhone_machineNumR/3043586","_from":"mobilePhone/2149319","_to":"MachineNum/2964843","_rev":"_YtgBdi---_","relation":"申请注册","link_type":33,"weight":0.3}
import json
import codecs
import random
import csv
def w_code():
    csvFile = open("F:\TEST3\mobilePhone_machineNumR.csv", "w", newline="",encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow([":START_ID(mobilePhone-ID)", ":END_ID(MachineNum-ID)","relation", "link_type","weight",":TYPE"])  # 写入列的名称
    # 写入多行用writerows                                #写入多行
    for i in range(1,101):
        ID = "mobilePhone_machineNumR/" + str(i)
        # key = i
        from_c = str(i)
        some = random.sample(range(1, 101), 2)
        if i not in some:
            b = [str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                writer.writerow([from_c,body,"申请注册", 33, 0.3,"mobilePhone_machineNumR"])
    csvFile.close()

w_code()