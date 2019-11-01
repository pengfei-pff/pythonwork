#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import  unittest
import  time as t
import  os



def getHeaders():
    '''获取headers'''
    return {'Content-Type':'application/json;charset=UTF-8','Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}

def login():
    '''把token写入到文件中'''
    r = requests.post(
        url=self.url + 'login',
        json={"username": "autoapi", "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
              "role": 2},
        headers=getHeaders(), timeout=5)
    with open(base_dir(), 'w') as f:
        f.write(r.json()['data']['token'])


def base_dir():
    '''获取当前文件的目录'''
    return os.path.join(os.path.dirname(__file__), 'token.md')

def getToken():
    '''读取存储在文件中的token'''
    with open(base_dir(),'r') as f:
        return f.read()

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.url='https://ecapi.parkingwang.com/v4/'

    def tearDown(self):
        t.sleep(1)

    def test_infoGet(self):
        '''验证:测试infoGet接口是否正确'''
        r = requests.post(url=self.url+'infoGet',json={"token": getToken()},headers=getHeaders(), timeout=5)
        self.assertEqual(r.json()['status'],0)
        self.assertEqual(r.json()['data']['username'],'autoapi')

    def test_isSoonExpire(self):
        '''验证：测试isSoonExpire接口是否正确'''
        r = requests.post(url=self.url+'isSoonExpire',json={"token":getToken()},headers=getHeaders(), timeout=5)
        self.assertEqual(r.json()['status'],0)
        self.assertEqual(r.json()['data']['expire'],False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
