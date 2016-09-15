import scrapy

from tutorial.items import NewsItem

class FreebufNewsSpider(scrapy.Spider):
    name = "freebuf_news"
    allowed_domains = ["freebuf.com"]

    def start_requests(self):
        for i in range(1, 3):
            yield scrapy.Request('http://www.freebuf.com/page/' + str(i), callback = self.parse)
            
    def parse(self, response):
        for sel in response.xpath('//div[@class="news-info"]'):
            item = NewsItem()
            item['title'] = sel.xpath('dl/dt/a/text()').extract()[0].strip()
            item['author'] = sel.xpath('dl/dd[1]/span[@class="name"]/a/@title').extract()
            item['date'] = sel.xpath('dl/dd[1]/span[@class="time"]/text()').extract()
            item['content'] = sel.xpath('dl/dd[@class="text"]/text()').extract()
            item['tags'] = sel.xpath('div/span[@class="tags"]/a/text()').extract()
            yield item
