# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:52:49 2018

@author: ya0guang , sharpstar
"""


import requests
import time
import re
import sys
# fill in this pls!
username = '';
password = '';

session = requests.session()
request = session.get('https://cas.xjtu.edu.cn/login')
request = request.text
str = 'name="lt" value="(.*?)"'
pattern = re.compile(str, re.S)
lt = re.findall(pattern, request)

print('登录中请稍候')       
str2 = u'登录'
str2 = str2.encode('utf-8','ignore')
postdata = {
    'username': username,
    'password': password,
    'code': '',
    'lt': lt[0],
    'execution': 'e1s1',
    '_eventId': 'submit',
    'submit': str2
}

res = session.post('https://cas.xjtu.edu.cn/login', postdata)
str1 = '''<div id="msg">(.*?)</div>'''
pattern1 = re.compile(str1, re.S)
response = re.findall(pattern1,res.text)
if(len(response) == 0):
    print('账号密码错误')
    sys.exit()
response = re.findall(pattern1,res.text)[0]

print(re.findall(pattern1,res.text)[0])
# for test
courseID = 1252
ccID = 753
classID = 55

#courseList: (courseID, ccID)
courseList = {(753, 627), (754, 627), (755,627), (756, 627), (1252, 753), \
              (1255, 757), (1256, 756), (1257, 755), (1258, 755), \
              (1259, 755), (1260, 755), (1261, 755), (1262, 754)}

postData = {"courseID": courseID, "watchTime": watchTime, "ccID": ccID, "classID": classID}

headers = {"Host": "xjtudj.edu.cn", \
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",\
          "Accept": "application/json, text/javascript, */*; q=0.01", \
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", \
          "Accept-Encoding": "gzip, deflate", \
          "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7"}

url = "http://xjtudj.edu.cn/course/course_updateUserWatchRecord.do"

for course in courseList:
    (courseID, ccID) = course
    print(course)
    for watchTime in range(0, 5200, 60):
        postData = {"courseID": courseID, "watchTime": watchTime, "ccID": ccID, "classID": classID}
        r = requests.session().post(url,data=postData,headers=headers)
        time.sleep(0.1)

print("welcome to xjtu 0w1 cybersecurity club")
