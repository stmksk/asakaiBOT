# coding: utf-8

import json
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


@respond_to('[sprint|Sprint][0-9]*$')
def burndown(message):
    textbody = message.body['text']
    pattern = r'[0-9]*$'
    sprintNum = int(re.search(pattern, textbody).group()) + 94
    message.send("https://dev.liferobotics.jp/redmine/rb/burndown/" + str(sprintNum))

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

