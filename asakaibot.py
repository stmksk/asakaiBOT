from slacker import Slacker
import json
import random

slackjson = open("slack.json").read()
settings =  json.loads(slackjson)

slack = Slacker(settings['token'])
members = settings['members']
random.shuffle(members)

# Send a message to #test channel
slack.chat.post_message(
        type="message",
        channel='#test',
        text="今日の朝会は["+" ▶ ".join(members)+"]の順です。\n"+
        "司会は["+members[0]+"]さんお願いします。",
        as_user=True)
