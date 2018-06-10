# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:48:50 2018

@author: Sharpstar,ya0guang
"""

import requests,sys
import re
import time


username = ''
password = ''
service = 'http%3A%2F%2Fxjtudj.edu.cn%2Fpcweb%2Fcas.jsp'
url = "https://cas.xjtu.edu.cn/login?service=%s" % service

k = requests.session()
r = k.get(url,headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"})
#得到重定向后的新url,表单要提交到新的url上才有效
new_url = r.url
print(new_url)
str1 = 'name="lt" value="(.*?)"'
pattern = re.compile(str1, re.S)
lt = re.findall(pattern, r.text)
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
#先提交表单
res = k.post(new_url,data = postdata)
#刷新一次以获取跳转页面
res1 = k.get(new_url)
#在跳转页面中获取跳转网页
str2 = 'content= "5;url=(.*?)"'
jump_url = re.findall(str2,res1.text)[0]
print(jump_url)
result = k.get(jump_url)

if(result.status_code == 200):
    print('login success!')
else:
    print('%d登录失败!(可能当前时间段访问量过大，重试即可)'%result.status_code,result.text)
    sys.exit()
    
#至此已经登录成功

sessionID = result.cookies["JSESSIONID"]

# for test
courseID = 1252
ccID = 753
classID = 55
watchTime = 59
#courseList: (courseID, ccID)
courseList = {(753, 627), (754, 627), (755,627), (756, 627), (1252, 753), \
              (1255, 757), (1256, 756), (1257, 755), (1258, 755), \
              (1259, 755), (1260, 755), (1261, 755), (1262, 754)}
              
#皮一下，选修都看完？
#courseList.update({(i,717) for i in range(1147,1153)}).update({(i,737) for i in range(1201,1205)}).update({(i,742) for i in range(1233,1241)})
postData = {"courseID": courseID, "watchTime": watchTime, "ccID": ccID, "classID": classID}

headers = {"Host": "xjtudj.edu.cn", \
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",\
          "Accept": "application/json, text/javascript, */*; q=0.01", \
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", \
          "Accept-Encoding": "gzip, deflate", \
          "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7"}
cookie = {'route': '', "JSESSIONID": sessionID}
url = "http://xjtudj.edu.cn/course/course_updateUserWatchRecord.do"

for course in courseList:
    (courseID, ccID) = course
    print(course,"完成度\n[",end="")
    for watchTime in range(0, 5200, 60):
        postData = {"courseID": courseID, "watchTime": watchTime, "ccID": ccID, "classID": classID}
        r = requests.post(url,data=postData, cookies=cookie, headers=headers)
        time.sleep(0.1)
        print("-",end="")
    print("]")

print("welcome to xjtu 0w1 cybersecurity club!")
