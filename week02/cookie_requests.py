import pretty_errors
import requests
from fake_useragent import UserAgent
from lxml import etree
from time import sleep


def get_url_name(myurl):
    ua = UserAgent(verify_ssl=False)
    headers = {
        'User-Agent' : ua.random,
        'Referer' : 'https://www.solidot.org/logout'
    }

    s = requests.Session()
    # 会话对象：在同一个 Session 实例发出的所有实例之间保持 cookie；
    # 期间使用 urllib3 的 connection pooling 功能；
    # 向同一个主机发送多个请求，底层的 TCP 链接将会被重用，从而来带显著的性能提升。
    login_url = 'https://www.solidot.org/dologin'
    form_data = {
        # 'ck':'',
        # 'name':'12345@q.com',
        # 'password':'323423423423',
        # 'remember':'false',
        # 'ticket':''
        'username':'qclpython123',
        'passwd':'qpython',
        'busername':'' ,
        'site':'' ,
        'keep':'1'
    }

    response = s.post(login_url , data = form_data, headers = headers)
    # print('\n',response.json())
    # print('\nCookie:',response.headers.get('Set-Cookie'))

    # 登录后可以进行后续的请求
    # url1 = 'https://www.solidot.org/?issue=20201205'
    response_issue = s.get(myurl,headers=headers)
    # print('\n',response_issue.text)
    selector = etree.HTML(response_issue.text)
    # 新闻标题
    new_titles = selector.xpath('//div[@class="block_m"]/div[@class="ct_tittle"]/div[@class="bg_htit"]/h2/a/text()')
    # 新闻链接
    new_link = selector.xpath('//div[@class="block_m"]/div[@class="ct_tittle"]/div[@class="bg_htit"]/h2/a/@href')
    
    # print(new_titles)
    # 新闻时间
    new_time = selector.xpath('//div[@class="block_m"]/div[@class="talk_time"]/text()')

    with open('html/new.txt','a+') as f:
        # f.write(str(new_titles))  #不换行追加
        if new_time:
            # f.write('\n新闻发表于：'.join(new_time))
            f.write('\n'.join(new_titles).join(new_link))
        else:
            # f.write('\n'.join(new_titles).join(new_link))
            pass
            # end
            # 查了资料，关于open()的mode参数：
            # 'r'：读
            # 'w'：写
            # 'a'：追加
            # 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
            # 'w+' == w+r（可读可写，文件若不存在就创建）
            # 'a+' ==a+r（可追加可写，文件若不存在就创建）
            # 对应的，如果是二进制文件，就都加一个b就好啦：
            # 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'

if __name__ == '__main__':
    urls = tuple(f'https://www.solidot.org/?issue={20201205 - daynum}' for daynum in range(5))
    # print(urls)
    for page in urls:
        get_url_name(page)
        sleep(5)





