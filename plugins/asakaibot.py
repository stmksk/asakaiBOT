# coding: utf-8

import json
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

slackjson = open("slack.json").read()
settings =  json.loads(slackjson)
url_burndown = settings['URL_burndown']

@respond_to('[sprint|Sprint][0-9]*$')
def burndown(message):
    textbody = message.body['text']
    pattern = r'[0-9]*$'
    sprintNum = int(re.search(pattern, textbody).group()) + 94
    message.send(url_burndown + str(sprintNum))

"""
@respond_to('朝会ﾀﾞﾖ')
def asakai_order_func(message):
    members = settings['members_mention']
    shuffled = list(members.keys()); random.shuffle(list(members.keys()))
    message.send("今日の朝会は\n"+" ▶ ".join(shuffled)+"の順です。\n司会は["+shuffled[0]+" "+members[shuffled[0]]+"]さんお願いします。")
"""

@listen_to('ｱｻｶｲ')
def asakai_test(message):
    message.send("ｱｻｶｲ？")

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
