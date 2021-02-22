import requests
import re

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}


def get_page(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(
        r'<p class="source">.*?<a.*?>.*?</a><a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(
        r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(
        r'<div class="contson".*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>', '', content)
        contents.append(''.join(x.split()))
    poems = []
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)


def main():
    url = 'https://www.gushiwen.cn/default_{}.aspx'
    for i in range(1, 11):
        get_page(url.format(i))


if __name__ == '__main__':
    main()
