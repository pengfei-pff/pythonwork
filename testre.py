import requests
import unittest
from test import getToken
import hashlib
import json
import xlrd
import base64
from Crypto.Cipher import AES

# class Coding_Hash(object):
#     #md5的加密方式
#     def md5(str):
#         m = hashlib.md5()
#         m.update(str.encode("utf-8"))
#         print(m.hexdigest())
#         return m.hexdigest()
#
#     #汉字md5的加密方式
#     def md5GBK(str1):
#         m = hashlib.md5(str1.encode(encoding='gb2312'))
#         print(m.hexdigest())
#         return m.hexdigest()

#sha256的加密方式
def get_sha256(str):
    m = hashlib.sha256()
    m.update(str.encode("utf-8"))
    print(m.hexdigest())
    return m.hexdigest()

def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return str.encode(text)  # 返回bytes

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.url="https://fk-apics.geotmtai.com"
    def tearDown(self) :
        pass

    #  # 登录获取token
    # def test_get_token(self):
    #     url = self.url+"/auth/login"
    #
    #     payload = "{\"username\":\"pengfei1\",\"password\":\"111111\",\"dsign\":0}"
    #     headers = {
    #         'uno': "100005",
    #         'encrypted': "0",
    #         'cache-control': "no-cache",
    #         'Postman-Token': "805d12e0-9be9-4a0b-a3e4-3c4d98c999f9"
    #     }
    #     # 获取token的返回值
    #     response = requests.request("POST", url, data=payload, headers=headers).json()
    #     #token请求断言
    #     self.assertEqual(response['code'], '200')  # 断言
    #     self.assertEqual(response['msg'], '成功')  # 断言
    #     print(response)
    #     return response['data']['tokenId']
    def test_info_get_T40309(self):
    #验证T40309接口
        url = self.url+"/icbc/guard/api/query"

        # payload= {"realName": "丽丽","cid": "13488540894","idNumber": "371428199103136060","authCode": "123456aaabbbcccddd","innerIfType":"T40309"}
        # '''使用postman必须用utf-8转化一下'''
        # # payload["realName"] = get_sha256("丽丽")
        # # payload["cid"] = get_sha256("13488540894")
        # # payload = payload.encode('utf-8')
        # # print(payload)
        # payload = json.dumps(payload)
        headers = {
            'tokenId':getToken(),
            'digitalSignatureKey': "",
            'cache-control': "no-cache",
            'Postman-Token': "0e22b603-8374-4b02-bcf8-834e23bf8709"
        }
        book = xlrd.open_workbook(r"C:\Users\pengfei\Desktop\xlrd.xlsx")#打开excel文件
        sheet = book.sheet_by_index(0)#用索引获取excel的表格
        nrows = sheet.nrows #获取excel所有的行数
        for i in range(1,nrows):
            cid1 = sheet.cell_value(i,0)
            idNumber1 = sheet.cell_value(i,1)
            realName1 = sheet.cell_value(i,2)
            # print(cid1, idNumber1, realName1)#测试检查数据使用
            cid = get_sha256(cid1)
            idNumber = get_sha256(idNumber1)
            realName = get_sha256(realName1)
            # print(cid,idNumber,realName)#测试检查加密数据使用
            data = {"cid":cid,"idNumber":idNumber,"realName":realName}
            payload0 = {"authCode": "9279320000","data":json.dumps(data),"innerIfType": "KGH00002"}
            payload = json.dumps(payload0)
            print("加密前结果",payload)


            key = '8000001007115009'  # 密码
            aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
            encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(payload))), encoding='utf-8').replace('\n','')# 加密
            print("加密后结果",encrypted_text)
            # response = requests.request("POST", url, data=encrypted_text, headers=headers).json()
            # # self.assertEqual(response['code'], '200')  # 断言
            # # self.assertEqual(response['msg'], '成功')  # 断言
            # print("KGH00002请求结果:",response)
            # print("KGH00002解密结果:",response)
            # return response


        # def test_info_get_T40309():
        # #验证T40309接口连通性
        #     url = self.url+"/zxw/user/api/flatquery"
        #
        #     payload = "{\t\t\n  \"realName\": \"马文强\",\n  \"idNumber\": \"140109199301121012\",\n  \"cid\": \"15763608899\",\n  \"photo\": \"\",\n  \"innerIfType\": \"T40309\",\n  \"queryTime\": \"\",\n  \"driversLicenseNumber\": \"152128197211304513\",\n  \"billCalibrationCode\": \"617176\",\n  \"billCode\": \"011001900111\",\n  \"billNum\": \"91777099\",\n  \"billTime\": \"20190406\",\t\n  \"billAmountOfMoney\": \"0.17\",\n  \"ip\": \"94.191.99.63\",\n  \"authCode\": \"123456aaabbbcccddd\"\n}\n"
        #     payload = payload.encode('utf-8')
        #     headers = {
        #     'tokenId': test_get_token(),
        #     'digitalSignatureKey': "",
        #     'cache-control': "no-cache",
        #     'Postman-Token': "0e22b603-8374-4b02-bcf8-834e23bf8709"
        #     }
        #
        #     response = requests.request("POST", url, data=payload, headers=headers).json()
        #     return response

if __name__ == '__main__':
    unittest.main(verbosity=2)





