#coding: utf-8

import json
import random
from slacker import Slacker
from crontab import CronTab
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time

slackjson = open("slack.json").read()
settings =  json.loads(slackjson)
slack = Slacker(settings['token'])
members = settings['members_mention']


class JobConfig(object):



  def __init__(self, crontab):
    """
    :type crontab: crontab.CronTab
    :param crontab: 実行時間設定
    """

    self._crontab = crontab


  def schedule(self):
    """
    次回実行日時を取得する。
    :rtype: datetime.datetime
    :return: 次回実行日時を
    """

    crontab = self._crontab
    return datetime.now() + timedelta(seconds=math.ceil(crontab.next()))

  def next(self):
    """
    次回実行時刻まで待機する時間を取得する。
    :rtype: long
    :retuen: 待機時間(秒)
    """

    crontab = self._crontab
    return math.ceil(crontab.next())


def job_controller(crontab):
  """
  処理コントローラ
  :type crontab: str
  :param crontab: 実行設定
  """
  def receive_func(job):
    import functools
    @functools.wraps(job)
    def wrapper():

      jobConfig = JobConfig(CronTab(crontab))
      logging.info("->- 処理を開始しました。")

      while True:

        try:

          # 次実行日時を表示
          logging.info("-?- 次回実行日時\tschedule:%s" %
            jobConfig.schedule().strftime("%Y-%m-%d %H:%M:%S"))

          # 次実行時刻まで待機
          time.sleep(jobConfig.next())

          logging.info("-!> 処理を実行します。")

          # 処理を実行する。
          job()

          logging.info("-!< 処理を実行しました。")

        except KeyboardInterrupt:
          break

      logging.info("-<- 処理を終了終了しました。")
    return wrapper
  return receive_func


@job_controller("0 1 * * MON-FRI")
def job1():

    shuffled = list(members.keys()); random.shuffle(list(members.keys()))
    slack.chat.post_message(
        channel='#helpme_sw',
        text="今日の朝会は["+" ▶ ".join(shuffled)+"]の順です。\n"+
        "各自10:01 まで前日、本日の作業内容を下書きしてください。\n"+
        "司会は["+shuffled[0]+"]さんお願いします。",
        as_user=True)

@job_controller("1 1 * * MON-FRI")
def job2():

    slack.chat.post_message(
        channel='#helpme_sw',
        text="10:01 になりました。順番に報告お願いします！",
        as_user=True)

""" test用job
@job_controller("* * * * MON-FRI")
def job3():

    random.shuffle(list(members.keys()))
    slack.chat.post_message(
        channel='#test',
        text="[[[TEST]]]今日の朝会は["+" ▶ ".join(list(members.keys()))+"]の順です。\n"+
        "司会は[ "+list(members.keys())[0]+" "+members[list(members.keys())[0]]+" ]さんお願いします。",
        as_user=True)
"""

def main():
  """
  """

  # ログ設定
  logging.basicConfig(level=logging.DEBUG,
    format="time:%(asctime)s.%(msecs)03d\tprocess:%(process)d" +
      "\tmessage:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

  # 処理リスト作成
  jobs = [job1, job2]

  # 処理を並列に実行
  p = Pool(len(jobs))
  try:
    for job in jobs:
      p.apply_async(job)
    p.close()
    p.join()
  except KeyboardInterrupt:
    pass


if __name__ == "__main__":

  main()

