import scrapy
from mayfes import items

class SingleSpider(scrapy.Spider):
    name = "single"
    allowed_domains = ["search.yahoo.co.jp"]

    next_path1 = '//*[@id="pg"]/a[11]/@href'
    next_path2 = '//*[@id="pg"]/a[10]/@href'
    search_list_path = '//*[@id="web"]/ol/li'
    titles_path = 'a/text()'
    texts_path = 'div/text()'

    def start_requests(self):
        word = getattr(self, 'word', None)
        if (word is not None):
            urls = [
                "https://search.yahoo.co.jp/search?p={0}&dups=1&b={1}".format(word, x)
                for x in range(1,300,10)
            ]
        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        search_responses = response.xpath(SingleSpider.search_list_path)
        for search_response in search_responses:
            item = items.MayfesItem()
            item["title"] = [
                box.strip() for box in search_response.xpath(SingleSpider.titles_path).extract()]
            item["texts"] = [
                box.strip() for box in search_response.xpath(SingleSpider.texts_path).extract()]
            yield item
