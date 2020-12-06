import pretty_errors
import requests

s = requests.Session()

session_1 = '123123'
setcookieUrl = 'http://httpbin.org/cookies/set/sessioncookie/'
cookieUrl = 'http://httpbin.org/cookies'
s.get(setcookieUrl+session_1)    #实现session 信息的拼装参数化
r = s.get(cookieUrl)

print(f"\n\n本网站cookies 信息 ：\n{r.text}")

try:
    session_1 = '12345678900'
    with requests.Session() as s:
        s.get(setcookieUrl+session_1)   #验证session信息多次设置与输出获取展示
        print(s.get(cookieUrl).json())
except Exception:
    print("session 设置异常！！")




