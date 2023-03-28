import requests

if __name__=="__main__":
    #第一步：指定url
    url='https://www.sogou.com/'

    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    #第二步：发出请求
    #get方法会返回一个响应对象
    response=requests.get(url=url,headers=headers)

    #第三步：获取响应数据，
    #text返回的是字符串形式的响应数据
    page_text=response.text

    #第四步：持久化存储
    with open('d:/gongyf/data/out..html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬虫完毕")