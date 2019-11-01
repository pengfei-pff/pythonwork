import requests

class HttpMain():

    def post_main(self,url,payload,headers):
        response = requests.post(url, data=payload, headers=headers)
        return response
    def get_mian(self,url,payload,headers):
        response = requests.get(url, data=payload, headers=headers)
        return response
    def run_main(self,method,url=None,payload=None,headers=None):
        try:
            if method.lower() =='post':
                result = self.post_main(url,payload,headers)
            else:
                result = self.get_mian(url,payload,headers)
            return result
        except Exception as e:
            print("请求错误信息{0}".format(e))

if __name__ == "__main__":

    url = "http://10.111.23.148:9101/login"  # 请求地址
    payload = '{"account": "PFF11","ip": "string","password": "123456"}'  # 请求参数
    headers = {'Content-Type': "application/json"}
    run_result = HttpMain()
    result = run_result.run_main('post',url, payload=payload, headers=headers)
    print(result.json())






