#使用Python 库 requests 获取豆瓣影评
import pretty_errors
import requests
from pathlib import *
import pretty_errors
import sys
# PEP-8  编程规范
# Google Python 风格指引

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

try:
    response = requests.get(myurl,headers=header)
except requests.exceptions.ConnectTimeout as e:
    print(f"requests库超时 \n{e}")
    sys.exit(1)

print(response.text)
print(f'返回码：{response.status_code}')

#将网页内容存储到文件

#获得Python脚本的绝对路径
p = Path(__file__)
print("当前文件绝对路径：",p)
pyfile_path = p.resolve().parent
print("路径：",pyfile_path)
html_path = pyfile_path.joinpath('html')  #连接路径

print(html_path)
# sys.exit(0)

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

print(page)

try:
    with open(page,'w',encoding='utf-8') as f:
        f.write(response.text)
        print('文件写入成功')
except FileNotFoundError as e:
    print(f'文件无法打开,{e}')
except IOError as e:
    print(f'读写文件出错,{e}')
except Exception as e:
    print(e)