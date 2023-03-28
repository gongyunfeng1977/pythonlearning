#UA：User-Agent(请求载体的身份标识)
#UA伪装：门户用站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器
#说明是一个正常请求，反之，不可以请求

import requests
if __name__=="__main__":
    url='https://www.sogou.com/web?' #https://www.sogou.com/web?query=你好李焕英
    #处理url携带的参数:封装到字典中
    world=input('请输入搜索内容：')
    param={
        'query':world
    }
    #UA伪装
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    #对指定的url发起的请求对应的url是携带参数的,并且请求过程中处理了参数
    #url请求过程中动态拼接了param
    response=requests.get(url=url,params=param,headers=headers)

    page=response.text

    kw=world+'.html'
    with open(kw,'w',encoding='utf-8') as fp:
        fp.write(page)
    print("爬虫完毕")