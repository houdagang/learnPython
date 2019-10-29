import requests
from bs4 import BeautifulSoup

movies = []
num = 0
for i in range(10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    res = requests.get(url)
    #获取shuju
    data = BeautifulSoup(res.text,'html.parser')
    #解析
    #获取所有的电影的div块
    bs = data.find_all('div',class_='info')
    for d in bs:
        num = num + 1
        #标题
        title = d.find('span',class_='title').text
        #链接
        href = d.find('a')['href']
        #评语
        remark = d.find('p',class_='quote').text
        #导演，演员
        person = d.find('p').text
        info = str(num) +'、名称：'+title + '\n' + '链接：'+ href +'\n推荐语：'+remark + '\n'
        movies.append(info)
f1 = open('1.txt','w')

for mov in movies:
    print(mov)
    f1.write(mov)
f1.close()