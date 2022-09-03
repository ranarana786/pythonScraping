from scrapy import Spider
from scrapy import Request
import pandas as pd
from scrapy.utils import log
from scrapy.utils.response import open_in_browser
import re
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import os



class Business(Spider):
    name = 'business'
    allowed_domains = ['yelp.com']

    # Accepting the arguments  that are passed through the command line
    def __init__(self, category=None):
        self.category = category
        # os.environ['PATH'] += "C:\Selenium"
        # self.driver = Chrome()
        # self.driver.implicitly_wait(10)

    def start_requests(self):
        'https://yelp.com/'
        links_file = pd.read_csv('categories.csv').values

        for link in links_file:
            if self.category in link[1]:
                yield Request(link[1], callback=self.parse)

    def parse(self, response):
        log.logger.info(self.category)

        all_cards = response.xpath("//div[@data-testid = 'serp-ia-card']")
        base_url = 'https://www.yelp.com/'

        for data in all_cards:
            item_link = base_url + data.xpath('.//a/@href').get()
            yield Request(url=item_link, callback=self.item_data)
        next_page = response.xpath('//a[@aria-label = "Next"]/@href').get()
        yield Request(url=next_page,callback=self.parse)

    def item_data(self, response):
        # name of the resturant
        name = response.xpath("//h1[@class = 'css-dyjx0f']/text()").get()
        print(name)

        # Total reviews of the resturant
        reviews = response.xpath("//span[@class = ' css-1fdy0l5']")
        reviews = reviews[0].xpath('.//text()').get()
        print(reviews)

        # Phone number
        phone_number = response.xpath('//p[contains(text(),"Phone number")]//following-sibling::p/text()').get()
        print(phone_number)

        # website
        website = response.xpath('//p[contains(text(),"Business website")]//following-sibling::p//a/text()').get()

        #Location
        location1 = response.xpath('//address//text()').getall()
        location2 = response.xpath('//address//following-sibling::p/text()').getall()
        final_location = ",".join(location1 + location2)

        # Amenities and more
        # amenities = response.xpath('//section[@aria-label = "Amenities and More"]')




        item = {
            'Name': name,
            'Reviews': reviews,
            'Contact': phone_number,
            'Website' : website,
            'Location':final_location
        }
        yield item
