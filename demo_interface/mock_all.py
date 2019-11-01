from demo_interface.mock_test import mock_test
from demo_interface.http_requests import HttpMain

url = "http://10.111.23.148:9101/login"  # 请求地址
payload = '{"account": "PFF11","ip": "string","password": "123456"}'  # 请求参数
headers = {'Content-Type': "application/json"}
data = {"cat":"miaomiao"}
run_result = HttpMain()

res = mock_test(run_result.run_main,payload,url,'post',data)
print(res)