import requests
import re

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}

def get_page(url):
    response = requests.get(url,headers=HEADERS)
    text=response.text
    contents = re.findall(r'<div class="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    for content in contents:
        x = re.sub(r'<.*?>', '', content)
        print(''.join(x.split()))
        print('='*30)
    
    


def main():
    url = 'https://www.qiushibaike.com/text/page/{}/'
    for i in range(2,12):
        get_page(url.format(i))
        

if __name__ == '__main__':
    main()
    