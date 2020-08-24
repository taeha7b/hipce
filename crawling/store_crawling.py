import re, requests
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--single-process")

path = '/home/taehyun/Downloads/chromedriver'

main_url = 'http://hince.co.kr/store'

driver = webdriver.Chrome(path, options = chrome_options)
driver.implicitly_wait(5)
driver.get(main_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

store_list = soup.select('div.tab')

data = []

for idx in range(len(store_list)):
    store = store_list[idx].select_one('div.tab-body > div.content').get_text()
    data = store.split(' ')

for idx in range(len(store_list)):
    store_name = store_list[idx].select_one('div.tab-header > h3.store-name').get_text()
    address = store_list[idx].select_one('div.tab-header > span.store-address').get_text()
    store = store_list[idx].select_one('div.tab-body > div.content').get_text()

    business_day_regex = re.compile(r'[^ 가-힣]+')
    business_days = business_day_regex.sub('', store).strip()
    business_day_temp = business_days.split(' ')
    business_day = [data for data in business_day_temp if data != ""]

    contact_regex = re.compile(r'[0-9]+\-[0-9]+\-[0-9]+|\~[0-9]')
    opening_hour_regex = re.compile(r'[0-9]+\:[0-9]+')

    temp = business_day_regex.findall(store)

    for d in temp:
        if opening_hour_regex.match(d):
            opening_hour = d
            
        if contact_regex.match(d):
            contact = d

    dic = {
        'name': store_name,
        'address': address,
        'business_day': business_day,
        'opening_hour': opening_hour,
        'contact': contact
    }

    data.append(dic)

dataframe = pd.DataFrame(data[13:])
dataframe.to_csv('store_crawling.csv', columns = ['name', 'address', 'business_day', 'opening_hour', 'contact'], index = False)

driver.close()