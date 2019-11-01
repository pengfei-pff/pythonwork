#生成Account_customNumR表测试数据
#data={"_key":"3188943","_id":"Account_customNumR/3188943","_from":"Account/3088861","_to":"customNum/1995990","_rev":"_Ytf945e---","relation":"属于","link_type":21,"weight":0.2}
import json
import codecs
import random
import csv
def w_code():
    csvFile = open("F:\TEST3\Account_customNumR.csv", "w", newline="", encoding='utf-8')  # 创建csv文件
    writer = csv.writer(csvFile)  # 创建写的对象
    writer.writerow([":START_ID(Account-ID)", ":END_ID(customNum-ID)", "relation", "link_type", "weight", ":TYPE"])  # 写入列的名称
    # 写入多行用writerows                                #写入多行
    for i in range(0,1000):
        ID = "Account_customNumR/" + str(i+1)
        # key = i
        from_c = str(i+1)
        some = random.sample(range(0, 100),1)
        if i not in some:
            b = [ str(c) for c in some]
            # relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            # m = random.sample(relation, 1)
            for body in b:
                # data = {"_id":ID, "_from": from_c,"_to": body, "_rev": "_YtgBRzq--_", "relation": m, "link_type": 11,"weight": 0.9}
                writer.writerow([from_c, body,"属于",21,0.2,"Account_customNumR"])
    csvFile.close()

w_code()