import re

# import pandas as pd
#
# data_file = pd.read_csv('yelp_scrapper/categories.csv')
#
# for i in data_file.values:
#     resturant = re.findall('.*=restaurants.*',i[1])
#     if resturant:
#         print(resturant)
#     else:
#         print('none')

# phone = '(415) 566-6143'
#
# pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
# matcher = pattern.search(phone)
# print(matcher.string)

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
os.environ['PATH'] += "C:\Selenium"
driver = webdriver.Chrome()
driver.get('https://www.yelp.com/biz/kingdom-of-dumplings-san-francisco')
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//section[@aria-label = "Amenities and More"]//button').click()