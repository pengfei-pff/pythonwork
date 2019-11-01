# -*- coding: utf-8 -*-
# print(chr(65))
# print("中文".encode("utf-8"))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(len("abc"))
# print(len("中文".encode("utf-8")))
# print("age:%s .Gaga:%s" %("中国",1))
# s1 = 72
# s2 = 85
# r = s2 - s1
# print("成绩提升的百分点:{0:.1f}".format(r))
# classromate = ["小明","晓华","小丽","小结"]
# classromate.append("小刚")
# print(classromate[4])
# classromate.pop(1)
# print(classromate)
# age = 20
# if age > 18:
#     print("小明好帅啊")
#     print("uyuyi")
# elif age >6:
#     print("yayayayy")
# else:
#     print("edasfdtf")
# # birth = input("出生年纪：")
# # birth = int(birth)
# # if birth < 20:
# #     print("00后")
# # else:
# #     print("老头子好")
# # names = ["大哥哥","小姐姐","小妹妹"]
# # for name in names:
# #     print(name)
# sun = 0
# for i in range(101):
#     sun = sun + i
# print(sun)
# n = 1
# while n < 200:
#     if n > 20:
#         break
#     print(n)
#     n = n + 1
# print("END")
n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 ==0:
#         continue
#     # n = n + 1
#     print(n)
# d = {"name":"小明","age":25 }
# print(d["name"])
# print(d.get("shua",-1))
# s = set([3,5,7,9])
# print(s)
# s =[7,8,5,3,94,1,2,3]
# s.sort()
# print(s)
# def my_abs(x):
# #     if not isinstance(x,(int,float)):
# #         raise TypeError("参数错误")
# #     if x > 0:
# #         return x
# #     else:
# #         return -x
# # print(my_abs("a"))
# def power(x,n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = x * s
#     return s
#
# print(power(5))
# def calc(*numbers):
# #     sum = 0
# #     for n in numbers:
# #         sum = sum + n
# #     return sum
# # print(calc())

# def f1(a, b, c=0, *args, **kw):
#      print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# print(f1(1,2,3,"a","b",x = 99))
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score > 90:
#             return "A"
#         elif self.score > 60:
#             return "B"
#         else:
#             return "C"
# Lisa = Student("彭飞",20)
# print(Lisa.name,Lisa.get_grade())

# print(type(123456))

# if name == username:
#     while count < 3:
#         pwd = input(请输入您的密码)
#         if pwd == password:
#             print("欢迎登陆测试系统")
#             break
#         else:
#             print("密码错误")
#             count +=1
#     else:
#         print("您输入密码错误三次，账户已被锁定")
#         with open("file.text",mode=a+,encoding="utf-8") as f:
#             test = ("%s"%name)
#             f.writelines(test)
# else:
#         print("该用户不存在")

# f = open("token.md","r",encoding="utf-8")
# f2 = open("token.text","w",encoding="utf-8")
# for line in f:
#     if line == "张三":
#         line = line.replace("张三","李四")
#     f2.write(line)
# f.close()
# f2.close()
# g = (x * x for x in range(1,10))
# for i in g:
#     print(i)
#
# def fun(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n + 1
#     return 'done'
# data = fun(10)
# while True:
#     try:
#         x = next(data)
#         print("g:",x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
# import random
# print (random.randint(1,2))
# 装饰器难点
# def dubug(fun):
#     def wrapper():
#         print("DEBUG:enter{}()".format(fun.__name__))
#         return fun
#     return wrapper
# def say_hello():
#     print("hello")
# say_hello = dubug(say_hello)
#
# import os,sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

# import random
# checkcode = ""
# for i in range(6):
#     current = random.randrange(0,6)
#     if current == i:
#         tmp = chr(random.randint(65,90))
#     else:
#         tmp = random.randint(0,9)
#     checkcode+= str(tmp)
# print(checkcode)
# import re
#
# if re.search("abc$","456465abc"):
#     print("find")
# else:
#     print("none")
# class Role(object):
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#
#     def shot(self):
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self):
#         print("just bought %s" % self.weapon,self.name)
#
#
# r1 = Role('Alex', 'police', 'AK47') #生成一个角色
# r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色

# _*_coding:utf-8_*_

#
# import threading
# import time
#
#
# def sayhi(num):  # 定义每个线程要运行的函数
#
#     print("running on number:%s" % num)
#
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
#     t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例
#
#     t1.start()  # 启动线程
#     t2.start()  # 启动另一个线程
#
#     print(t1.getName())  # 获取线程名
#     print(t2.getName())
#
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a)
#         a, b = b, a + b
#
# print(fib(10))

# class Point(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def reste(self):
#         print("hahshdf",self.name)
#
# p1 = Point("hahah",45)
# print(p1.reste())
import socket
# ip_port = ('127.0.0.1',9999)
# sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
# sk.bind(ip_port)
#
# while True:
#     data = sk.recv(1024)
#     print(data.decode())
#
# import threading
# class Didn(object):
#     def __init__(self,name,job):
#         self.name = name
#         self.job = job
#     def music(self,tat):
#         print("music is open",self.name)
#     def move(self):
#         print("moving is going",self.job)
# didn = Didn("xihaua",12)
# th1 = threading.Thread(target= didn.music,args=())
# th2 = threading.Thread(target= didn.move,args=())
# th1.start()
# th2.start()
# print ("all over ")
# from time import ctime,sleep
# def music():
#     for i in range(2):
#         print("I was listening to music. %s" %ctime())
#         sleep(1)
#
# def move():
#     for i in range(2):
#         print("I was at the movies! %s" %ctime())
#         sleep(5)
#
# # if __name__ == '__main__':
# music()
# move()
# print("all over %s" %ctime())
#coding=utf-8
import threading
# from time import ctime,sleep
#
# def music(func):
#     for i in range(2):
#         print("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print("I was at the %s! %s" %(func,ctime()))
#         sleep(5)
#
#
#
# if __name__ == '__main__':
#     music('爱情买卖')
#     move('阿凡达')
#
#     print("all over %s" %ctime())


#coding=utf-8
import threading
# coding=utf-8
# from time import sleep, ctime
# import threading
#
# def muisc(func):
#     for i in range(2):
#         print('Start playing： %s! %s' % (func, ctime()))
#         sleep(2)
#
#
# def move(func):
#     for i in range(2):
#         print('Start playing： %s! %s' % (func, ctime()))
#         sleep(5)
#
#
# def player(name):
#     r = name.split('.')[1]
#     if r == 'mp3':
#         muisc(name)
#     else:
#         if r == 'mp4':
#             move(name)
#         else:
#             print( 'error: The format is not recognized!')
#
# list = ['11111111.mp3', '222222222.mp4']
#
# threads = []
# files = range(len(list))
# # 创建线程
# for i in files:
#     t = threading.Thread(target=player, args=(list[i],))
#     threads.append(t)
# print(threads)
# if __name__ == '__main__':
#     # 启动线程
#     for i in files:
#         t.setDaemon(True)
#         threads[i].start()
# for i in files:
#     threads[i].join()
# #     t.join()
# # 主线程
# print('end:%s' %ctime())
# import os
# print(os.getcwd())
# import sys
# print(sys.platform)

# import requests
# data = {
#     "name":"zhaofan",
#     "age":22
# }
# response = requests.get("http://httpbin.org/get",params=data)
# print(response.url)
# print(response.text)

# #coding:utf-8
# import os
# import time
# import codecs
#
# #切换到创建文件目录
# os.chdir(r"C:\Users\pengfei\Desktop\TEST")
#
# #新建创建文件函数
# def create_file():
#
# #构造文件名：以“年月日”为文件名的.dat文件
#     t=time.localtime()
#     file_name=time.strftime("%Y-%m-%d",t)+".csv"
#     #创建并打开文件
#     # fp=open(file_name,'w+')
#
#     with codecs.open(file_name,'a',encoding='utf-8') as fp:
#     #写入文件内容
#         # fp.write(codecs.BOM_UTF8)
#         # s = "12345\n"
#         fp.writelines('12345\n')
#         fp.writelines(['67890\n'])
#         fp.write('中国')
#     #关闭文件
#     # fp.close()
#
# #调用函数
# create_file()

# #coding=utf-8
# import json
# import os
#
# os.chdir(r"C:\Users\pengfei\Desktop\TEST")
# books = [
#     {
#         'title': 'Python基础',
#         'price': '79.00'
#     },
#     {
#         'title': 'Scrapy网络爬虫',
#         'price': '56.00'
#     }
# ]
#
# json_str = json.dumps(books, ensure_ascii=False)
#
# with open('books.json', 'w') as fp:
#     fp.write(json_str)
# coding=utf-8



# 将字典内容进行排序
# import collections
# dic = collections.OrderedDict()
# dic = dict()
# dic['_key'] = "4190404"
# dic['_id'] = "customNumSelfR/4190404"
# dic['_from'] = "customNum/1969513"
# dic['_to'] = "customNum/1969576"
# dic['_rev'] = "_YtgBRzq--_"
# dic['relation'] = ["兄弟"]
# dic['relation'] = 11
# dic['relation'] = 0.9
# # print("dic is:",dic.items())

# for i in range(1, 10):
#     fvm = "customNum/" + str(i)
#     some = random.sample(range(1, 100000), 3)
#     if i not in some:
#         b = ["customNum/" + str(c) for c in some]
#         relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
#         n = random.randint(1, 1)
#         m = random.sample(relation, n)
#         for body in b:
#             writer.writerow([fvm, body, m])
import json
import codecs
import random
def w_code():

    for i in range(1,100):
        ID = "customNumSelfR/" + str(i+1)
        # key = i
        from_c = "customNum/" + str(i+1)
        some = random.sample(range(1, 100), 2) #随机从1-100中取两个值，生成2个值的列表
        if i not in some:    #防止from_c，_to相同
            b = ["customNum/" + str(c) for c in some]
            relation = ["家人", "兄弟", "子女", "母子", "父母", "父子", "父女", "母女"]
            m = random.sample(relation, 1)
            for body in b:
                # key = 1
                data = {"_id":ID, "_from": from_c,
                        "_to": body, "_rev": "_YtgBRzq--_", "relation": m, "link_type": 11,
                        "weight": 0.9}
                json_str = json.dumps(data, ensure_ascii=False)
                print(json_str)
                with codecs.open(r'F:\TEST2\customNumSelfR.jsonl', 'a',
                                 encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
                    f.write(json_str)
                    f.write('\n')  # 如果循环写入多个json数据需要加一个换行符

w_code()
# # data ={"_key":"4190404","_id":"customNumSelfR/4190404","_from":"customNum/1969513","_to":"customNum/1969576","_rev":"_YtgBRzq--_","relation":["兄弟"],"link_type":11,"weight":0.9}
# data ={"_key":"4190404","_id":"customNumSelfR/4190404","_from":"customNum/1969513","_to":"customNum/1969576","_rev":"_YtgBRzq--_","relation":["兄弟"],"link_type":11,"weight":0.9}
# json_str = json.dumps(data,ensure_ascii=False)
# print(json_str)
# with codecs.open(r'C:\Users\pengfei\Desktop\TEST\data.jsonl', 'a',encoding="utf-8") as f:  # ‘a’表示在不删除原数据的情况下在文件末尾写入数据
#     f.write(json_str)
#     f.write('\n')  # 如果循环写入多个json数据需要加一个换行符