import scrapy
from .. import items

class SystemSpider(scrapy.Spider):
    name = "system"
    allowed_domains = ["search.yahoo.co.jp"]
    start_urls = [
        "https://search.yahoo.co.jp/search?p=東京大学+システム創成学科&dups=1&b={0}".format(x)
        for x in range(1,1000,10)
    ]

    next_path1 = '//*[@id="pg"]/a[11]/@href'
    next_path2 = '//*[@id="pg"]/a[10]/@href'
    # search_list_path = '//*[@id="web"]/ol/li'
    titles_path = '//*[@id="web"]/ol/li/a/text()'
    texts_path = '//*[@id="web"]/ol/li/div/text()'

    def parse(self, response):
        # search_responses = response.xpath(TodaiSpider.search_list_path)
        # for search_response in search_responses:
        todai = items.MayfesItem()
        todai["title"] = [
            box.strip() for box in response.xpath(SystemSpider.titles_path).extract()]
        todai["texts"] = [
            box.strip() for box in response.xpath(SystemSpider.texts_path).extract()]
        yield todai

        # next_page = response.xpath(TodaiSpider.next_path1).extract_first() or response.xpath(TodaiSpider.next_path2).extract_first()
        # if next_page:
        #     url = response.urljoin(next_page)
        #     yield scrapy.Request(url, callback=self.parse)
