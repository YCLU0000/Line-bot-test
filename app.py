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
#import time



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
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
        
# 處理位置資訊
@handler.add(MessageEvent, message=LocationMessage)
def handle_message(event):
    address = event.message.address
    lat = event.message.latitude
    long = event.message.longitude
    carousel_message = TemplateSendMessage(
    alt_text = "food_category",
    template = CarouselTemplate(
    columns=[
        CarouselColumn(
        thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg", # thumbnail for the message
        title = "請問你想吃甚麼種類?",
        text = "請點選以下一個選項",
        actions = [
            MessageAction(
            label = "日式料理",
            text = "日式料理"),
            MessageAction(
            label = "韓式料理",
            text = "韓式料理"),
            MessageAction(
            label = "中式料理",
            text = "中式料理")
        ])
    ]))
    line_bot_api.reply_message(event.reply_token, carousel_message)
        
    

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    # First Filter : Food category
    # Click one action in the picture list at the bottom of line
    if bool(re.search("美食搜尋", message)):
        quick_message = TextSendMessage(
        text = "請分享你現在的位置給我 :",
        quick_reply = QuickReply(items = [QuickReplyButton(action=LocationAction(label="傳送位置"))])
        )
        line_bot_api.reply_message(event.reply_token, quick_message)
        
    # Second filter : stars
    # One variable from pervious filter needs to be record : food category
    elif bool(re.search("日式|韓式|中式", message)): # if detect "日式|韓式|中式"
        food_category = event.message.text
        carousel_message = TemplateSendMessage(
        alt_text = "stars",
        template = CarouselTemplate(
        columns=[
            CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg", # thumbnail for the message
            title = "請問你想找幾星的餐廳?",
            text = "請點選以下一個選項",
            actions = [
                MessageAction(
                label = "三星以上",
                text = "三星以上"),
                MessageAction(
                label = "四星以上",
                text = "四星以上")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, carousel_message)
    # Third filter : take out / inside
    # One variable from pervious filter needs to be record : star
    elif bool(re.search("星", message)): # if detect "star"
        stars = event.message.text
        carousel_message = TemplateSendMessage(
        alt_text = "takeout",
        template = CarouselTemplate(
        columns=[
            CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg", # thumbnail for the message
            title = "請問你想外帶還是內用?",
            text = "請點選以下一個選項",
            actions = [
                MessageAction(
                label = "內用", 
                text = "內用"),
                MessageAction(
                label = "外帶",
                text = "外帶")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, carousel_message)
    # forth filter : date
    # One variable from pervious filter needs to be record : takeout
    
    # five filter : display number
    # One variable from pervious filter needs to be record : date
    elif bool(re.search("內用|外帶", message)):
        time = str(datetime.date.today())
        carousel_message = TemplateSendMessage(
        alt_text = "display",
        template = CarouselTemplate(
        columns=[
            CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg",
            title = "你要顯示幾個結果?",#scrapping(event.message.text),
            text = "請點選以下一個選項",#scrapping(event.message.text),
            actions = [
                MessageAction(
                label = "0~5",
                text = "我要0~5個結果"),
                MessageAction(
                label = "6~10",
                text = "我要6~10個結果")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, carousel_message)
    # Showing results
    elif bool(re.search("結果" ,message)):
        carousel_message = TemplateSendMessage(
        alt_text = "results",
        template = CarouselTemplate(
        columns=[
            CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg",
            title = "這間餐廳很適合你!",#scrapping(event.message.text),
            text = "台北市 - 梨園湯包",#scrapping(event.message.text),
            actions = [
                URIAction(
                label = "點這裡去Google Map!",
                uri = "https://goo.gl/maps/nWsFPjAVzZtaFbgs5")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, carousel_message)
    
    
    print(event.message.type)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
