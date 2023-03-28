import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
response = requests.get(url,headers = headers)
response.encoding = 'utf-8'
content = response.content.decode('utf-8')#以字节流形式打印网页源码
soup = BeautifulSoup(response.text,'lxml')

#写文件
path2=r'file1.txt'
with open(path2,'w',encoding='utf-8') as f1:
    f1.write(soup.prettify())


#爬取选择网页文档的内容
data = soup.find_all(name = 'script',attrs = {'id':'getListByCountryTypeService2true'})
#转为字符串
account = str(data)
account1 = account[95:-21]#切片截取从52到后面倒数21取到需要的数据
account1_json = json.loads(account1)

path2=r'file2.txt'
with open(path2,'w',encoding='utf-8') as f1:
    f1.write(account)

path2=r'file3.txt'
with open(path2,'w',encoding='utf-8') as f1:
    f1.write(account1)


#提取数据到列表
id = []
continents = []
provinceName = []
currentConfirmedCount = []
confirmedCount = []
confirmedCountRank = []
suspectedCount = []
curedCount = []
deadCount = []
deadCountRank = []
deadRate = []
deadRateRank = []
print(len(account1_json))
i=0
for a in account1_json:
    if 'id' in a:
        id.append(a['id'])
    else:
        id.append('没有')
    continents.append(a['continents'])
    provinceName.append(a['provinceName'])
    currentConfirmedCount.append(a['currentConfirmedCount'])
    confirmedCount.append(a['confirmedCount'])
    if 'confirmedCountRank' in a:
        confirmedCountRank.append(a['confirmedCountRank'])
    else:
        confirmedCountRank.append('没有')
    suspectedCount.append(a['suspectedCount'])
    curedCount.append(a['curedCount'])
    deadCount.append(a['deadCount'])
    if 'deadCountRank' in a:
        deadCountRank.append(a['deadCountRank'])
    else:
        deadCountRank.append('没有')
    if 'deadRate' in a:
        deadRate.append(a['deadRate'])
    else:
        deadRate.append('没有')
    if 'deadRateRank' in a:
        deadRateRank.append(a['deadRateRank'])
    else:
        deadRateRank.append('没有')

#转换成pandas数组
df = {
    'id':pd.Series(id),
    '所在大洲':pd.Series(continents),
    '城市':pd.Series(provinceName),
    '当前确诊':pd.Series(currentConfirmedCount),
    '累计确诊':pd.Series(confirmedCount),
    '确诊排名':pd.Series(confirmedCountRank),
    '疑似病例':pd.Series(suspectedCount),
    '治愈人数':pd.Series(curedCount),
    '死亡人数':pd.Series(deadCount),
    '死亡人数排名':pd.Series(deadCountRank),
    '死亡率':pd.Series(deadRate),
    '死亡率排名':pd.Series(deadRateRank)
}
pds = pd.DataFrame(df)
pds.to_excel('1.xlsx', index=False)