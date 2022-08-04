# importing the selenium package
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# # This package will enable for installing the and adding the chrome manager directly
# from webdriver_manager.chrome import ChromeDriverManager

# Importing the time module
import time

# Importing the os module
import os

# importing the beautifulsoup package
from bs4 import BeautifulSoup

# Importing the pandas
import pandas as pd

# driver = webdriver.Chrome(ChromeDriverManager().install())

# Adding the Chrome driver in the path variable
os.environ['PATH'] += 'C:\Selenium'

# Initialize the chrome driver
driver = Chrome()

url = 'https://www.youtube.com/c/AddictedA1/videos'

# Requesting the page
driver.get(url)


# Maximize the window
driver.maximize_window()

while True:
    # Loop Will Be Run Untill The End Of The Page
    scroll_height = 2000
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight ")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")

    time.sleep(1.5)
    document_height_after = driver.execute_script("return document.documentElement.scrollHeight ")
    print(document_height_after, document_height_before)
    if document_height_after == document_height_before:
        break

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

videos = soup.find_all('div', attrs={"id": "dismissible"})

all_post = []

for v in videos:
    # dictionary for holding the whole data
    data_dict = {}
    # Title of the post
    data_dict['title'] = v.find('a', id='video-title').text
    # Post link
    data_dict['link'] = 'https://www.youtube.com/' + v.find('a', id='video-title')['href']
    # Post meta info
    meta = v.find('div', id="metadata-line").find_all('span')
    # Post Views
    data_dict['view'] = meta[0].text
    # Post upload date
    data_dict['age'] = meta[1].text

    all_post.append(data_dict)

print(all_post)

# Writing the data into the .csv and .excel file
data_frame = pd.DataFrame(all_post)

name = url.split('/')[-2]

data_frame.to_csv(f"{name}.csv")
data_frame.to_excel(f"{name}.xlsx")

# Navigate the cursor to the end of the page
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#
#     # Pausing the code
#     time.sleep(2)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         print('done height match')
#         break
#     last_height = new_height
