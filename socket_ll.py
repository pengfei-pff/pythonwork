# coding=utf-8
import csv
import random
import time
from multiprocessing import Process, Pool
import codecs


def w_code():
    '''第一个写完文件，第二个文件实现读取第一个文件生成另一个文件'''
    # os.chdir("C:\Users\pengfei\Desktop\TEST")
    csvFile = codecs.open(r"C:\Users\pengfei\Desktop\TEST\2222.csv", "w",
                          encoding='utf-8')  # 创建csv   文件写customNum表 newline=""
    # csvFile.write(codecs.BOM_UTF8)  # 防止乱码

    # writer = csv.writer(csvFile)  # 创建写的对象
    writer = csv.writer(csvFile, dialect="unix")

    # 先写入columns_name
    writer.writerow(["_from", "_to", "relationship"])  # 写入列的名称
    # 写入多行用writerows                                #写入多行

    for i in range(1, 10):
        fvm ="customNum/" + str(i)
        some = random.sample(range(1, 100000), 3)
        if i not in some:
            b = ["customNum/" + str(c) for c in some]
            relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            n = random.randint(1, 1)
            m = random.sample(relation, n)
            for body in b:
                writer.writerow([fvm, body, m])

            # writer.writerow([fvm, b, random.sample(relation, n)])
        # some = random.sample(range(1,10000000), 3)
        # if i not in some:
        #     b = [str(c) +"customNum/"for c in some]
        #     writer.writerow([fvm, b, random.sample(relation, n)])
    csvFile.close()


if __name__ == '__main__':
    pool = Pool()
    start_time = time.time()
    for i in range(5):
        pool.apply_async(func=w_code)
        # pool.apply(func=Foo, args=(i,))

    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    end_time = time.time()
    print('all_time', end_time - start_time)
