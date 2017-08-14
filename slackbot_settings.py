# coding: utf-8
import json

slackjson = open("slack.json").read()
settings =  json.loads(slackjson)


# botアカウントのトークンを指定
API_TOKEN = (settings['token'])

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "?"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
