import pandas as pd
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    product_list = soup.select('div.xans-element-.xans-product.xans-product-normalpackage > div > div > ul > li')

    for product_list_idx in range(len(product_list)):

        product_url = product_list[product_list_idx].select_one('div.product-image > a')['href']
        driver.get(main_url + product_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        product = soup.select_one('li.product-name.xans-record- > span').get_text()

        iframe_url = soup.select_one('iframe#crema-product-reviews-1')['src']
        driver.get(iframe_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        review_list = soup.select('div.page > ul > li')

        for review_idx in range(len(review_list)):

            user = review_list[review_idx].select_one('div > div.products_reviews_list_review__info_container > ul > li > div.products_reviews_list_review__info_value').get_text()

            images = []
            image_list = review_list[review_idx].select('li.products_reviews_list_review__image')
            for image_idx in range(len(image_list)):
                image = image_list[image_idx].select_one('a > img')['src']
                images.append('http:' + image)

            content = review_list[review_idx].select_one('div.products_reviews_list_review__message > a > div:nth-child(1)').get_text().strip()

            score = review_list[review_idx].select_one('div.products_reviews_list_review__score_text_rating').get_text()

            try:
                total = review_list[review_idx].select_one('div.products_reviews_list_review__score_like_result js-like-result > span > strong.js-like-score-total').get_text()
                like = review_list[review_idx].select_one('div.products_reviews_list_review__score_like_result js-like-result > span > strong.js-like-score-plus').get_text()
            except:
                total = 0
                like = 0

            dislike = int(total) - int(like)

            dic = {
                'user': user,
                'product': product,
                'images': images,
                'content': content,
                'score': score,
                'total': total,
                'like': like,
                'dislike': dislike
            }

            data.append(dic)

        while True:
            try:
                driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[3]/div/div/a[11]').click()
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                review_list = soup.select('div.page > ul > li')

                for review_idx in range(len(review_list)):

                    user = review_list[review_idx].select_one('div > div.products_reviews_list_review__info_container > ul > li > div.products_reviews_list_review__info_value').get_text()

                    images = []
                    image_list = review_list[review_idx].select('li.products_reviews_list_review__image')
                    for image_idx in range(len(image_list)):
                        image = image_list[image_idx].select_one('a > img')['src']
                        images.append('http:' + image)

                    content = review_list[review_idx].select_one('div.products_reviews_list_review__message > a > div:nth-child(1)').get_text().strip()

                    score_text = review_list[review_idx].select_one('div.products_reviews_list_review__score_text_rating').get_text()
                    score = score_text[score_text.find('-') + 1:]


                    try:
                        total = review_list[review_idx].select_one('div.products_reviews_list_review__score_like_result js-like-result > span > strong.js-like-score-total').get_text()
                        like = review_list[review_idx].select_one('div.products_reviews_list_review__score_like_result js-like-result > span > strong.js-like-score-plus').get_text()
                    except:
                        total = 0
                        like = 0

                    dislike = int(total) - int(like)

                    dic = {
                        'user': user,
                        'product': product,
                        'images': images,
                        'content': content,
                        'score': score,
                        'total': total,
                        'like': like,
                        'dislike': dislike
                    }

                    data.append(dic)

            except:
                break

dataframe = pd.DataFrame(data)
dataframe.to_csv('review_crawling.csv', columns = ['user', 'product', 'images', 'content', 'score', 'total', 'like', 'dislike'], index = False)

driver.close()