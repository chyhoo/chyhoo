import requests
from lxml import etree

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}


def get_temp(url):
    temps = []
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)
    tables = html.xpath("//div[@class='conMidtab']")[0].xpath(".//table")
    for table in tables:
        trs = table.xpath(".//tr")[2:]
        for index,tr in enumerate(trs):
            city = tr.xpath(".//td")[0].xpath("./a/text()")[0]
            if index == 0:
                city = tr.xpath(".//td")[1].xpath("./a/text()")[0] 
            temperature = tr.xpath(".//td")[-2].xpath("./text()")[0]
            temp = {
                '城市': city,
                '温度': temperature
            }
            temps.append(temp)
    return temps


def spider():
    url_hb = "http://www.weather.com.cn/textFC/hb.shtml"
    temps = get_temp(url_hb)
    for temp in temps:
        print(temp)
    print(len(temps))


if __name__ == '__main__':
    spider()
