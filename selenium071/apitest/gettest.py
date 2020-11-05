import  requests
# 不带参数的get
# url = 'http://47.112.110.1:8082/scm/purchase-suggestion/saveSuggestion'
# r = requests.get(url)
# print(type(r.text))
# print(eval(r.text))
#-----------------------------------------
#带参数的get
url = 'http://scm.demo.mstemes.com/scm/delivery-note-link-plan/getReceipInfotByNoteNo/'
params = {"deliveryNoteNo":"A02001-20200826-001",
          "purTenantCode":"169"}
r = requests.get(url = url,params=params)
print(type(r.text))
print(eval(r.text))
