from slacker import Slacker
import json
slacktoken = open("slack.json").read()
token =  json.loads(slacktoken)

slack = Slacker(token['token'])

# Send a message to #general channel
slack.chat.post_message('#test', 'Hello fellow slackers!', as_user=True)
