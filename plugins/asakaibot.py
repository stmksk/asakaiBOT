# coding: utf-8

import json
import random
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

@listen_to('朝会ダヨ')
def asakai_order_func(message):
    slackjson = open("slack.json").read()
    settings =  json.loads(slackjson)
    members = settings['members']
    random.shuffle(members)
    message.send("今日の朝会は\n"+" ▶ ".join(members)+"の順です。\n司会は["+members[0]+"]さんお願いします。")

@listen_to('ｱｻｶｲ')
def asakai_test(message):
    message.send("ｱｻｶｲ？")
