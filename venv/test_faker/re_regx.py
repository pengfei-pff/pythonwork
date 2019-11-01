import re
pattm=re.compile('a{1,2}',re.S)   #最少匹配1个a,最多匹配两个a
pstr=pattm.findall('fcabcdaaaef^')
if pstr!=None:
    print(pstr)
else:
    print('无匹配!')
