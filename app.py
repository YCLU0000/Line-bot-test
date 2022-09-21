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

# variable setting
category = ""
star = ""
takeout = ""
shownumber = ""
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
            PostbackAction(
            label = "日式料理",
            data = "A日式料理"),
            PostbackAction(
            label = "韓式料理",
            data = "A韓式料理"),
            PostbackAction(
            label = "中式料理",
            data = "A中式料理")
        ]),
        CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg", # thumbnail for the message
            title = "請問你想找幾星的餐廳?",
            text = "請點選以下一個選項",
            actions = [
                PostbackAction(
                label = "三星以上",
                data = "B三星以上"),
                 PostbackAction(
                label = "四星以上",
                data = "B四星以上")
            ]),
        CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg", # thumbnail for the message
            title = "請問你想外帶還是內用?",
            text = "請點選以下一個選項",
            actions = [
                PostbackAction(
                label = "內用",
                data = "C內用"),
                PostbackAction(
                label = "外帶",
                data = "C外帶")
            ]),
        CarouselColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg",
            title = "你要顯示幾個結果?",
            text = "請點選以下一個選項",
            actions = [
                PostbackAction(
                label = "0~5",
                data = "D0~5"),
                PostbackAction(
                label = "6~10",
                data = "D6~10")
            ])
    ]))
    line_bot_api.reply_message(event.reply_token, carousel_message)
        
    
@handler.add(PostbackEvent):
    data = event.postback.data
    filt = ["種類", "星數", "內用/外帶", "顯示餐廳數"]
    if data[0] == "A" : # 種類
        category = data[2:]
    elif data[0] == "B" : # 星
        star = data[2:]
    elif data[0] == "C" : # 內用/外帶
        takeout = data[2:]
    elif data[0] == "D" : # 數目
        shownumber = data[2:]
    
    # 回應文字
    answer = pd.DataFrame({'answer' : [category, star, takeout, shownumber]})
    missing = (answer['answer'].values == "").sum()
    if all(answer['answer']) :
        message = "你已經全部選擇完畢 :\n種類 = {}\n星數 = {}\n內用/外帶 = {}\n顯示餐廳數 = {}".format(category, star, takeout, shownumber)
        line_bot_api.reply_message(event.reply_token, message)
    else not(all(answer['answer'])) :
        message = "你目前已選擇 :\n"
        pos = 0
        for answer in answer['answer']:
            if answer != "" :
                message = "%s%s: %s\n" % (message, filt[pos], answer)
                pos = pos + 1
            elif answer == "" :
                pos = pos + 1
    message = message + "你還有%s項還沒有選擇"%(missing)
    line_bot_api.reply_message(event.reply_token, message)    
        
    #print(event.message.type)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
