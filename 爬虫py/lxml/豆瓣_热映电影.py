import requests
from lxml import etree
import csv

# 1.将目标网站上的页面抓取下来 
headers = {
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
    "Referer":"https://www.douban.com/" 
}

url = "https://movie.douban.com/cinema/nowplaying/ganzhou/"
response = requests.get(url,headers=headers)
text = response.text

# 2.将抓取下来的数据根基一定的规则进行提取
html = etree.HTML(text)

ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'thumbnail': thumbnail
    }
    movies.append(movie)
    
for i in range(len(movies)):
    print(movies[i],'\n')
    
titles=['title','score','duration','region','director','actors','thumbnail']
with open('豆瓣_热映电影.csv','w',encoding='utf-8') as fp:
    writer = csv.DictWriter(fp,titles)
    writer.writeheader()
    writer.writerows(movies)
