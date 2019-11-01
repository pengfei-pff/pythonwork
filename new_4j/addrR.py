#data = {"_key":"7663610","_id":"AddrR/7663610","_from":"customNum/1977098","_to":"Addr/7528880","_rev":"_YueeQca--_","relation":[221],"link_type":22,"weight":0.3}
import json
import codecs
import random
import csv
def w_code():
    csvFile = open("F:\TEST3\AddrR.csv", "w", newline="", encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow([":START_ID(customNum-ID)", ":END_ID(Addr-ID)", "relation", "link_type", "weight", ":TYPE"])  # 写入列的名称
    # 写入多行用writerows                                #写入多行
    for i in range(0,400,3):
        ID = "AddrR/" + str(i+1)
        # key = i
        from_c = str(i+1)
        some = random.sample(range(1, 1000),2)
        if i not in some:
            b = [ str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                writer.writerow([from_c, body, [221], 22, 0.3, "AddrR"])
    csvFile.close()
w_code()