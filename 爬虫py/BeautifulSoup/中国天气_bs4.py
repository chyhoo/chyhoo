import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}

temps = []


def get_temp(url):
    global temps
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find("div", class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all("tr")[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all("td")
            city = list(tds[0].stripped_strings)[0]
            if index == 0:
                city = list(tds[1].stripped_strings)[0]
            temp = {
                '城市': city,
                '最低温度': list(tds[-2].stripped_strings)[0]
            }
            print(temp)
            temps.append(temp)


def main():
    urls = ["http://www.weather.com.cn/textFC/hb.shtml",
            "http://www.weather.com.cn/textFC/db.shtml",
            "http://www.weather.com.cn/textFC/hd.shtml",
            "http://www.weather.com.cn/textFC/hz.shtml",
            "http://www.weather.com.cn/textFC/hn.shtml",
            "http://www.weather.com.cn/textFC/xb.shtml",
            "http://www.weather.com.cn/textFC/xn.shtml",
            "http://www.weather.com.cn/textFC/gat.shtml"]
    for url in urls:
        get_temp(url)


def write_csv():
    titles = ['城市', '最低温度']
    with open('中国天气.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, titles)
        writer.writeheader()
        writer.writerows(temps)


def drawing():
    data = pd.read_csv('.\\中国天气.csv')
    data['最低温度'] = data['最低温度'].astype(int)
    temp_top10 = data.groupby('城市')['最低温度'].max().sort_values(ascending=False)[:10]
    temp_top10.plot.bar()
    plt.show()


if __name__ == '__main__':
    main()
    write_csv()
    drawing()
