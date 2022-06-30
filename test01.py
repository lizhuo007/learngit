#-*- coding:utf-8 -*-
import requests 
import json
from urllib import parse

# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# Form_Data = {}
# Form_Data['type'] = 'AUTO'
# Form_Data['i'] = '今天'
# Form_Data['doctype'] = 'json'
# Form_Data['xmlVersion'] = '2.1'
# Form_Data['keyfrom'] = 'fanyi.web'
# Form_Data['action'] = 'FY_BY_CLICKBUTTON'


# data = parse.urlencode(Form_Data).encode('utf-8')
# response = requests.post(url, data = data)
# print(response.url)

URL = "http://www.baidu.com/{category}/{page}/"
category = "foot"
page = "10"
new_url = URL.format(category = category, page = page)
print(new_url)


print("Hello {1}, your balance is {0}.".format("Adam", 230.2346))

name ="Eric"
print(f"My name is {name}")
# content = response.content.decode("utf-8")

# # print(response)
# print(json.loads(content))

# print(content)

