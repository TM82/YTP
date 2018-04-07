import scrapy
from mayfes import items

class AlmightySpider(scrapy.Spider):
    name = "almighty"
    allowed_domains = ["search.yahoo.co.jp"]

    next_path1 = '//*[@id="pg"]/a[11]/@href'
    next_path2 = '//*[@id="pg"]/a[10]/@href'
    search_list_path = '//*[@id="web"]/ol/li'
    titles_path = 'a/text()'
    texts_path = 'div/text()'

    def start_requests(self):
        word = getattr(self, 'word', None)
        univ_name = getattr(self, 'univ_name', None)
        if (word is not None) and (univ_name is not None):
            urls = [
                "https://search.yahoo.co.jp/search?p='{0}'+'{1}'&dups=1&b={2}".format(word, univ_name, x)
                for x in range(1,300,10)
            ]
        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        search_responses = response.xpath(AlmightySpider.search_list_path)
        for search_response in search_responses:
            item = items.MayfesItem()
            item["title"] = [
                box.strip() for box in search_response.xpath(AlmightySpider.titles_path).extract()]
            item["texts"] = [
                box.strip() for box in search_response.xpath(AlmightySpider.texts_path).extract()]
            yield item

        # next_page = response.xpath(AlmightySpider.next_path1).extract_first() or response.xpath(AlmightySpider.next_path2).extract_first()
        # if next_page:
        #     url = response.urljoin(next_page)
        #     yield scrapy.Request(url, callback=self.parse)
