from flask import Flask, request, abort

from linebot import (
        LineBotApi, WebhookHandler
)
from linebot.exceptions import (
        InvalidSignatureError
)
from linebot.models import *

# scrap package
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from parsel import Selector
import datetime
import re
import numpy as np
import pandas as pd
import os

def scrapping(key_word) :
    key_food = '火鍋106'
    key_place = key_word
    # options setting
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    url = 'https://www.google.com/maps/search/{0}+near+{1}'.format(key_food, key_place)
    driver.get(url)
    page_content = driver.page_source
    response = Selector(page_content)

    results = []

    for el in response.xpath('//div[contains(@aria-label, "的搜尋結果")]/div/div[./a]'):
        results.append({
            'link': el.xpath('./a/@href').extract_first(''),
            'title': el.xpath('./a/@aria-label').extract_first('')
            #'type': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div//span[text()="·"]/following::span/text()').extract_first(),
            #'rating': el.xpath('div//span[contains(@aria-hidden, "true")]/text()').extract_first(''),
            #'reviewsCount': el.xpath('div//span[contains(@aria-hidden, "true")]/following::text()').extract_first(''),
            # 'service'
            # response.xpath('//div[contains(@aria-label, "的搜尋結果")]/div//div[contains(@class, "UaQhfb fontBodyMedium")]').extract_first('')
            #'address': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div//span[@jsan="0.aria-hidden"]/following::span/text()').extract_first(),
            #'status': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div[3]//span[text()="·"]/following::span/text()').extract_first(),
            #'nextOpenTime': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div[3]//span[text()="·"]/following::span[4]/text()').extract_first()
        })


    search_result = [a['title'] for a in results]
    picked_result = search_result[3]
    #target_url = [a['link'] for a in results if a['title'] == picked_result]
    #driver.get(target_url[0])
    #to refresh the browser
    #driver.refresh()

    # search results of related blogs
    #driver.quit()
    # return
    return(picked_result)
print(scrapping("台北市"))
