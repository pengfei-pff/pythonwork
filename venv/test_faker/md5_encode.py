# import json
# import hashlib
# from collections import OrderedDict
#
# param={"inputCodes":["6932608700850"],
# "terminal":{"status":1,"channel":"D002","storeCode":"2107",
# "passage":"D002","storeName":"Python全栈自动化","identity":"","maxProductCount":5,"posId":"D002"}}
#
# dict_2=OrderedDict()
# for item in param:
#     # print(type(item))
#     if type(item)==dict:
#         dict_sub=OrderedDict()
#         for key in item:
#             dict_sub[key]=item[key]
#         dict_2[item]=dict_sub
#     else:
#         dict_2[item]=param[item]
# print(dict_2)
# str_data=json.dumps(dict_2)
#
# def md5Encode(param):
#     client_secret='F0897E16-5D1E-4A31-9644-BBF974E2DD88'#此为加密的秘钥
#     sign=param+client_secret
#     m = hashlib.md5(sign.encode(encoding='utf-8'))
#     return m.hexdigest().upper()
#
# print(md5Encode(str_data))


from collections import OrderedDict
param={"inputCodes":["6932608700850"],
"terminal":{"status":1,"channel":"D002","storeCode":"2107",
"passage":"D002","storeName":"Python","identity":"","maxProductCount":5,"posId":"D002"}}
dict_2=OrderedDict()
for item in param:
    if type(item)==dict:
        dict_sub=OrderedDict()
        for key in item:
            dict_sub[key]=item[key]
        dict_2[item]=dict_sub
    else:
        dict_2[item]=param[item]
#最后得到的dict_2就是排序过后的字典

print(dict_2)