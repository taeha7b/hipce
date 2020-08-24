import csv, requests
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--single-process")


path = '/home/taehyun/Downloads/chromedriver'

main_url = 'http://hince.co.kr'

driver = webdriver.Chrome(path, options = chrome_options)
driver.implicitly_wait(5)
driver.get(main_url + '/category/lipstick/48')
soup = BeautifulSoup(driver.page_source, 'html.parser')

data = []

category_list = soup.select('div.category-list > a')

for category_list_idx in range(len(category_list)):
    category_url = category_list[category_list_idx]['href']

    driver.get(main_url + category_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    category_image_sub = category_list[category_list_idx].select_one('img')['src']
    category_image = main_url + category_image_sub

    category_name = category_list[category_list_idx].select_one('span').get_text()

    product_list = soup.select('div.xans-element-.xans-product.xans-product-normalpackage > div > div > ul > li')

    for product_list_idx in range(len(product_list)):

        product_name = product_list[product_list_idx].select_one('div.product-info > div.name > a > span').get_text()

        tag_image = []

        try:
            tag_image_list = product_list[product_list_idx].select_one('div.product-info > div.product-icons > img')['src']
            tag_image.append(main_url + tag_image_list)
        except:
            pass
        
        image_list = []


        primary_image = product_list[product_list_idx].select_one('div.product-image > a > img.primary-image')['src']
        secondary_image = product_list[product_list_idx].select_one('div.product-image > a > img.secondary-image')['src']


        image_list.append(main_url + primary_image)
        image_list.append(main_url + secondary_image)

        product_price = product_list[product_list_idx].select_one('div.product-info > div.price > span').get_text()

        product_url = product_list[product_list_idx].select_one('div.product-image > a')['href']
        driver.get(main_url + product_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        outer_margin = soup.select_one('div.product-section.product-detail > div')

        description_image_list = outer_margin.findAll('img')

        description_images = []

        for description_idx in range(len(description_image_list)):
            description_image = description_image_list[description_idx]['src']
            description_images.append(main_url + description_image)

        dic = {
            'category': category_name,
            'category_image': category_image,
            'name': product_name,
            'price': product_price,
            'image': image_list,
            'tag': tag_image,
            'description_image': description_images
        }

        data.append(dic)

    next_page = soup.select_one('a.hince-icon.next-icon')['href']
    if next_page != '#none':
        driver.get(main_url + category_url + next_page)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        product_list = soup.select('div.xans-element-.xans-product.xans-product-normalpackage > div > div > ul > li')

        for product_list_idx in range(len(product_list)):

            product_name = product_list[product_list_idx].select_one('div.product-info > div.name > a > span').get_text()

            tag_image = []

            try:
                tag_image_list = product_list[product_list_idx].select_one('div.product-info > div.product-icons > img')['src']
                tag_image.append(main_url + tag_image_list)
            except:
                pass
            
            image_list = []


            primary_image = product_list[product_list_idx].select_one('div.product-image > a > img.primary-image')['src']
            secondary_image = product_list[product_list_idx].select_one('div.product-image > a > img.secondary-image')['src']


            image_list.append(main_url + primary_image)                                                                                            
            image_list.append(main_url + secondary_image)

            product_price = product_list[product_list_idx].select_one('div.product-info > div.price > span').get_text()

            product_url = product_list[product_list_idx].select_one('div.product-image > a')['href']
            driver.get(main_url + product_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            outer_margin = soup.select_one('div.product-section.product-detail > div')

            description_image_list = outer_margin.findAll('img')

            description_images = []

            for description_idx in range(len(description_image_list)):
                description_image = description_image_list[description_idx]['src']
                description_images.append(main_url + description_image)

            dic = {
                'category': category_name,
                'category_image': category_image,
                'name': product_name,
                'price': product_price,
                'image': image_list,
                'tag': tag_image,
                'description_image': description_images
            }

            data.append(dic)
            
dataframe = pd.DataFrame(data)
dataframe.to_csv('shop_crawling.csv', columns = ['category', 'category_image', 'name', 'price', 'image', 'tag', 'description_image'], index = False)

driver.close()