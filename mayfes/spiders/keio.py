import scrapy
from mayfes import items

class KeioSpider(scrapy.Spider):
    name = "keio"
    allowed_domains = ["search.yahoo.co.jp"]
    start_urls = [
        "https://search.yahoo.co.jp/search?p=慶應義塾大学&dups=1&b={0}".format(x)
        for x in range(1,1000,10)
    ]

    next_path1 = '//*[@id="pg"]/a[11]/@href'
    next_path2 = '//*[@id="pg"]/a[10]/@href'
    search_list_path = '//*[@id="web"]/ol/li'
    titles_path = 'a/text()'
    texts_path = 'div/text()'

    def parse(self, response):
        search_responses = response.xpath(KeioSpider.search_list_path)
        for search_response in search_responses:
            item = items.MayfesItem()
            item["title"] = [
                box.strip() for box in search_response.xpath(KeioSpider.titles_path).extract()]
            item["texts"] = [
                box.strip() for box in search_response.xpath(KeioSpider.texts_path).extract()]
            yield item

        # next_page = response.xpath(KeioSpider.next_path1).extract_first() or response.xpath(KeioSpider.next_path2).extract_first()
        # if next_page:
        #     url = response.urljoin(next_page)
        #     yield scrapy.Request(url, callback=self.parse)
