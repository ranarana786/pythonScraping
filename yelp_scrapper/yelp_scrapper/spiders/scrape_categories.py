from scrapy import Spider
from scrapy import Request
from scrapy.utils.response import open_in_browser
from scrapy.utils import log


class Categories(Spider):
    name = 'cate'
    allowed_domains = ['yelp.com']

    start_urls = ['https://yelp.com/']

    def parse(self, response):
        # category container
        categories = response.xpath('//div[@aria-label = "Category Navigation Section"]')

        # All Categories Tab
        categories_card = categories.xpath('.//*[@class = " arrange-unit__09f24__rqHTg border-color--default__09f24__NPAKY"]')

        # All categories_link
        for data in categories_card:
            # category_name
            category_name = data.xpath('.//p/text()').get()

            # category link
            category_url = data.xpath('.//a/@href').get()
            category_url = response.urljoin(category_url)

            # Data Item
            item = {'Name':category_name,'Link Address':category_url}
            yield item







        # log.logger.info(categories)

