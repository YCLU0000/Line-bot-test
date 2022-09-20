#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
import time



#### scrap code #####
# search results from google map
def scrapping(key_word) :
    key_food = '火鍋106'
    key_place = key_word
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.google.com/maps/search/{0}+near+{1}'.format(key_food, key_place)
    driver.get(url)
    page_content = driver.page_source
    response = Selector(page_content)

    results = []

    for el in response.xpath('//div[contains(@aria-label, "的搜尋結果")]/div/div[./a]'):
        results.append({
            'link': el.xpath('./a/@href').extract_first(''),
            'title': el.xpath('./a/@aria-label').extract_first(''),
            'type': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div//span[text()="·"]/following::span/text()').extract_first(),
            'rating': el.xpath('div//span[contains(@aria-hidden, "true")]/text()').extract_first(''),
            'reviewsCount': el.xpath('div//span[contains(@aria-hidden, "true")]/following::text()').extract_first(''),
            # 'service'
            # response.xpath('//div[contains(@aria-label, "的搜尋結果")]/div//div[contains(@class, "UaQhfb fontBodyMedium")]').extract_first('')
            'address': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div//span[@jsan="0.aria-hidden"]/following::span/text()').extract_first(),
            'status': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div[3]//span[text()="·"]/following::span/text()').extract_first(),
            'nextOpenTime': el.xpath('div//div[contains(@class, "UaQhfb fontBodyMedium")]//div[contains(@class, "W4Efsd")]/following::div[3]//span[text()="·"]/following::span[4]/text()').extract_first()
        })

    #print(results)

    search_result = [a['title'] for a in results]
    picked_result = search_result[3]
    #target_url = [a['link'] for a in results if a['title'] == picked_result]
    #driver.get(target_url[0])
    #to refresh the browser
    #driver.refresh()

    # search results of related blogs
    driver.quit()
    # return
    return(picked_result)


#### app
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('MzvgoVaHfTUK+DnR87rdf1dGIFGZW7fgZvpdkxGmWzDkpD41ffYQKd1VTG7YQprU90boy+x+aS8bpu0WjrKcMkLm+bSq3U4BMD8yHmxUAucxKGAY0eQn4uG5sbvuc9J4xYtZUrX4jBf2b6lrZbO+YgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('dc03f0c538f730509807c0065dac48cf')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
        

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    if "結果" in message :
        carousel_message = TemplateSendMessage(
        alt_text = "results",
        template = CarouselTemplate(
        columns=[
            CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg",
            title = "請問你想吃甚麼種類?",
            text = "請點選其中一個種類",
            actions = [
                MessageAction(
                label = "台北市",
                text = "台北市"),
                MessageAction(
                label = "台北市",
                text = "台北市")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, carousel_message)
    elif message == "台北市":
        carousel_message = TemplateSendMessage(
        alt_text = "results",
        template = CarouselTemplate(
        columns=[
            CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg",
            title = "台北市",#scrapping(event.message.text),
            text = "台北市",#scrapping(event.message.text),
            actions = [
                MessageAction(
                label = "台北市",
                text = "台北市"),
                MessageAction(
                label = "台北市",
                text = "台北市")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, carousel_message)
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
