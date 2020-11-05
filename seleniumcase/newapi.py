import requests
import unittest
import sys
#这个是登录请求的地址
from nose.tools import assert_equal

loginUrl = \
    'http://scm.demo.mstemes.com/auth/oauth/token?username=ADMIN' \
    '&password=usJkn2OypDaSxAqS%2B1Gjlw%3D%3D&' \
    'randomStr=68261598604678418&code=&grant_type=password&scope=server'
headers = {"Content-Type":"application/json","Authorization":"Basic bXN0ZTptc3Rl",
           "isToken":"false","TENANT-ID":"147"}
data = {
    "username":"ADMIN",
    "password":"usJkn2OypDaSxAqS%2B1Gjlw%3D%3D",
}
#这个是请求的参数，一般是用户名和密码，实际的key和value以实际为准
params = {'username':'kuaiyu','password':123456}
#开始发送请求
r = requests.post(url=loginUrl,json=data,headers=headers)
#查看返回码信息
reponse = r.text
print(r.text)
print(r.status_code)
#比较返回码是否200
assert_equal(r.status_code,200)
# assert_equal ("6998b7fb-292c-447e-9f1a-36bc11dde058",reponse)
print(r.status_code)
