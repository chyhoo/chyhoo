import requests
import re

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}


def get_detail_message(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    title = re.findall(
        r'<h4 data-v-288d7ecc class="recruit-title">(.*?)</h4>', text)[0]
    print(title)


def spider():
    base_url = "https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006&index={}"
    for i in range(1, 8):
        print('第', i, "页")
        print("=" * 30)
        base_url.format(i)
        break


if __name__ == '__main__':
    spider()
