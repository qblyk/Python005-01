import pretty_errors
import requests

# http 协议的 get 方法

# r = requests.get('https://github.com')
# r.status_code
# r.headers['content-type']
# r.encoding

# r.json
# print(r.text)

# http 协议的 POST 方法
# import requests

r = requests.post('http://httpbin.org/post', data = {'key':'value'})

print(r.json())