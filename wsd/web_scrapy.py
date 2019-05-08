import requests
from bs4 import BeautifulSoup
from pyltp import SentenceSplitter

class WebScrape(object):
    def __init__(self, word, url):
        self.url = url
        self.word = word

    def web_parse(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                                             (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        req = requests.get(url=self.url, headers=headers)

        # 解析网页，定位到main-content部分
        if req.status_code == 200:
            soup = BeautifulSoup(req.text.encode(req.encoding), 'lxml')
            return soup
        return None


    def get_gloss(self):
        soup = self.web_parse()
        if soup:
            lis = soup.find('ul', class_="polysemantList-wrapper cmn-clearfix")
            if lis:
                for li in lis('li'):
                    if '<a' not in str(li):
                        gloss = li.text.replace('▪', '')
                        return gloss

        return None

    def get_content(self):
        # 发送HTTP请求
        result = []
        soup = self.web_parse()
        if soup:
            paras = soup.find('div', class_='main-content').text.split('\n')
            for para in paras:
                if self.word in para:
                    sents = list(SentenceSplitter.split(para))
                    for sent in sents:
                        if self.word in sent:
                            sent = sent.replace('\xa0', '').replace('\u3000', '')
                            result.append(sent)

        result = list(set(result))

        return result

    def write_2_file(self):
        gloss = self.get_gloss()
        result = self.get_content()
        print(gloss)
        print(result)
        if result and gloss:
            with open('./%s_%s.txt'% (self.word, gloss), 'w', encoding='utf-8') as f:
                f.writelines([_+'\n' for _ in result])

    def run(self):
        self.write_2_file()

#url = 'https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%B0%8F%E7%B1%B3%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/3250213?fromtitle=%E5%B0%8F%E7%B1%B3&fromid=1566828#viewPageContent'
#url = 'https://baike.baidu.com/item/%E5%B0%8F%E7%B1%B3/17756#viewPageContent'
#WebScrape('小米', url).run()

#url = 'https://baike.baidu.com/item/%E8%8B%B9%E6%9E%9C/5670?fr=aladdin'
#url = 'https://baike.baidu.com/item/%E8%8B%B9%E6%9E%9C%E5%85%AC%E5%8F%B8/304038?fromtitle=%E8%8B%B9%E6%9E%9C&fromid=6011224#viewPageContent'
#WebScrape('苹果', url).run()

#url = 'https://baike.baidu.com/item/%E4%BC%91%E6%96%AF%E6%95%A6%E7%81%AB%E7%AE%AD%E9%98%9F/370758?fromtitle=%E7%81%AB%E7%AE%AD&fromid=8794081#viewPageContent'
#url = 'https://baike.baidu.com/item/%E7%81%AB%E7%AE%AD/6308#viewPageContent'
#WebScrape('火箭', url).run()

#url = 'https://baike.baidu.com/item/%E9%9F%A9%E5%9B%BD/6009333?fr=aladdin'
url = 'https://baike.baidu.com/item/%E9%9F%A9%E5%9B%BD/6009300#viewPageContent'
WebScrape('韩国', url).run()