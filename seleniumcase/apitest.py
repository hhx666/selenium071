import requests
import unittest
# #这个是登录请求的地址
# loginUrl = 'http://47.112.110.1:8090/login'
# #这个是请求的参数，一般是用户名和密码，实际的key和value以实际为准
# params = {'username':'kuaiyu','password':123456}
# #开始发送请求
# response = requests.post(url=loginUrl,params=params)
# #以下按照需要打印出来先调试
# print(type(response.request.headers),response.request.headers) #获取请求头
# print(type(response.headers),response.headers) #获取响应头
# print(type(response.cookies),response.cookies)#获取响应cookie
# print(type(response.url),response.url) #获取响应url
# print(type(response.request.url),response.request.url) #获取请求url
# print(response.content.decode())#打印返回的内容并转码

#这个是登录请求的地址
loginUrl = 'http://47.112.110.1:8082/scm/purchase-suggestion/saveSuggestion'
headers = {"Content-Type":"application/json"}
data = {"purchaseSuggestionNo":"200.0",
"productCode":"001",
"productName":"喇叭线",
"spc":"100",
"purchaseUnit":"个",
"qty":"9999",
"supplierCode":"168",
"remark":"zhazha交界口",
"requireDate":"2020-09-03 00:00:00",
"purTenantCode":"168"}
#这个是请求的参数，一般是用户名和密码，实际的key和value以实际为准
params = {"purchaseSuggestionNo":"200.0",
"productCode":"001",
"productName":"喇叭线",
"spc":"100",
"purchaseUnit":"个",
"qty":"9999",
"supplierCode":"168",
"remark":"zhazha交界口",
"requireDate":"2020-09-03 00:00:00",
"purTenantCode":"168"
}
#开始发送请求
r = requests.post(url=loginUrl,json=data,headers=headers)
#查看返回码信息
reponse = r.text
print(r.text)
print(r.status_code)
#比较返回码是否200
assert True
# assert ("true",reponse)
print(r.status_code)


#
# #以下按照需要打印出来先调试
# print(type(response.request.headers),response.request.headers) #获取请求头
# print(type(response.headers),response.headers) #获取响应头
# print(type(response.cookies),response.cookies)#获取响应cookie
# print(type(response.url),response.url) #获取响应url
# print(type(response.request.url),response.request.url) #获取请求url
# print(response.content.decode())#打印返回的内容并转码