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
    if "隨機找店家" in message :
        carousel_message = TemplateSendMessage(
        alt_text = "food_cate",
        template = CarouselTemplate(
        columns=[
            CarouseColumn(
            thumbnail_image_url = "https://www.iberdrola.com/documents/20125/39904/real_food_746x419.jpg",
            title = "請問你想吃甚麼種類?",
            text = "請點選其中一個種類",
            actions = [
                MessageAction(
                label = "日式料理",
                text = "日式料理"),
                MessageAction(
                label = "中式料理",
                text = "中式料理")
            ])
        ]))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(carousel_message))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
