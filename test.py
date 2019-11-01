import os
import requests
'''登录获取token，把token存放到当前目录下'''

# 登录获取token
def test_get_token():
    url = "http://10.111.32.169:90/auth/login"

    payload = "{\"username\":\"pengfei2\",\"password\":\"111111\",\"dsign\":0}"
    headers = {
        'uno': "100013",
        'encrypted': "0",
        'cache-control': "no-cache",
        'Postman-Token': "805d12e0-9be9-4a0b-a3e4-3c4d98c999f9"
    }
    # 获取token的返回值
    response = requests.request("POST", url, data=payload, headers=headers)

    # token请求断言
    # self.assertEqual(response['code'], '200')  # 断言
    # self.assertEqual(response['msg'], '成功')  # 断言
    print(response.json())
    with open(base_dir(), 'w') as f:
        f.write(response.json()['data']['tokenId'])
    return ("sucess")


def base_dir():
    '''获取当前文件的目录'''
    return os.path.join(os.path.dirname(__file__), 'token.md')


def getToken():
    '''读取存储在文件中的token'''
    with open(base_dir(), 'r') as f:
        return f.read()

if __name__ == '__main__':
    print(test_get_token())