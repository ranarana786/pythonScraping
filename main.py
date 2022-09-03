import re

import pandas as pd

data_file = pd.read_csv('yelp_scrapper/categories.csv')

for i in data_file.values:
    resturant = re.findall('.*=restaurants.*',i[1])
    if resturant:
        print(resturant)
    else:
        print('none')
