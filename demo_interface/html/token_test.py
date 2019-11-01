"""
Created on 2019年04月03日
@author:
"""

import time
import hashlib
import requests
import operator
import json

appKey = "n3nuk67byade3c3qgrccjhosvmqfzt7z5wavp3ig"

appSecret = "b3a3056ef7ffb441332892ed76998b2e"

time_stamp = str(int(time.time()))

url = "http://10.10.10.100:8080/rest/v1/token/get"


class get_tokenclass():

    # 生成字符串
    def str_create(self):
        if operator.lt(appKey[0], appSecret[0]) == bool(1):           #py3中operator类和py2中cmp()函数的作用相似，通过比较2个值的大小，返回布尔类型
            strnew = time_stamp + appKey + appSecret
        else:
            strnew = time_stamp + appSecret + appKey
        print(strnew)
        return strnew


    # 生成signature
    def signature_create(self):
        str_switch = self.str_create()
        signature = hashlib.sha1(str_switch.encode('utf-8')).hexdigest().upper().strip()
        print(signature)
        return signature


    # 生成token
    def token_creat(self):
        signature = self.signature_create()
        params = {"appKey":appKey, "timestamp":time_stamp, "signature":signature}
        res = requests.get(url=url,params=params)
        print(res.url)
        print(json.loads(res.content.decode('utf-8')))
        token = json.loads(res.content.decode('utf-8'))['result']['token']           #字节型的response转换成字符串型，再转换成字典型
        print(token)
        return token


if __name__ == '__main__':
    tc = get_tokenclass()
    # str_create()
    # signature_create()
    tc.token_creat()
    # tc.str_create()
    # tc.signature_create()