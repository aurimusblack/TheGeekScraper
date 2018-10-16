import scrapy
from googlesearch import search
class linksParser(scrapy.Spider):
    count = 1
    name = "LinksParser"
    start_urls = ['https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/']
    
    def getPage(self, response):
        print('hi')
        filename = 'problem'+str(self.count)+'.html'
        self.count = self.count + 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parse(self, response):
        topics = response.css('div.entry-content ol li a::text').extract()
        for x in topics[0 : len(topics) - 5]:
            y = x.encode("utf-8")
            print(y)
            for k in search(y + ' site:geeksforgeeks.org',stop=1):
                print(k)
                yield response.follow(k, callback=self.getPage)
                break


