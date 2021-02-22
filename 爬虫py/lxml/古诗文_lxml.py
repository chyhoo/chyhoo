import requests
from lxml import etree

HEADERS = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}


def get_page(url):
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)
    conts = html.xpath("//div[@class='sons']//div[@class='cont']")
    for cont in conts:
        try:
            title = cont.xpath("./p")[0].xpath("./a/b/text()")[0]
            dynasty = cont.xpath("./p")[1].xpath("./a")[1].xpath("./text()")[0]
            author = cont.xpath("./p")[1].xpath("./a")[0].xpath("./text()")[0]
            contents = cont.xpath("./div[@class='contson']//text()")
            content_=''
            for x in contents:
                content_=content_+x
                content=''.join(content_.split())
            print(content)
            poems=[]
            poem={
                    'title':title,
                    'dynasty':dynasty,
                    'author':author,
                    'content':content
                }
            poems.append(poem)
            for poem in poems:
                print(poem)            
        except:
            pass

def main():
    url = 'https://www.gushiwen.cn/default_{}.aspx'
    for i in range(1, 11):
        get_page(url.format(i))
        

if __name__ == '__main__':
    main()
