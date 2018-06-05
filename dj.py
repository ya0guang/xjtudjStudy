import requests
import time

courseID = 1252
ccID = 753
classID = 55
sessionID = ""

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
cookie = {'route': '', "JSESSIONID": sessionID}
url = "http://xjtudj.edu.cn/course/course_updateUserWatchRecord.do"

for course in courseList:
    (courseID, ccID) = course
    print(course)
    for watchTime in range(0, 5200, 60):
        postData = {"courseID": courseID, "watchTime": watchTime, "ccID": ccID, "classID": classID}
        r = requests.post(url,data=postData, cookies=cookie, headers=headers)
        time.sleep(0.1)
        print(course, r.text)
