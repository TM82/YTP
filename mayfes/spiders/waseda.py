import scrapy
from .. import items

class WasedaSpider(scrapy.Spider):
    name = "waseda"
    allowed_domains = ["search.yahoo.co.jp"]
    start_urls = [
        "https://search.yahoo.co.jp/search?p=早稲田大学&dups=1&b={0}".format(x)
        for x in range(271,1000,10)
    ]

    next_path1 = '//*[@id="pg"]/a[11]/@href'
    next_path2 = '//*[@id="pg"]/a[10]/@href'
    # search_list_path = '//*[@id="web"]/ol/li'
    titles_path = '//*[@id="web"]/ol/li/a/text()'
    texts_path = '//*[@id="web"]/ol/li/div/text()'

    def parse(self, response):
        # search_responses = response.xpath(WasedaSpider.search_list_path)
        # for search_response in search_responses:
        item = items.MayfesItem()
        item["title"] = [
            box.strip() for box in response.xpath(WasedaSpider.titles_path).extract()]
        item["texts"] = [
            box.strip() for box in response.xpath(WasedaSpider.texts_path).extract()]
        yield item

        # next_page = response.xpath(WasedaSpider.next_path1).extract_first() or response.xpath(WasedaSpider.next_path2).extract_first()
        # if next_page:
        #     url = response.urljoin(next_page)
        #     yield scrapy.Request(url, callback=self.parse)
