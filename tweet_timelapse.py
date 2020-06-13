#!/usr/bin/env python
import twitter
import time
import datetime
import os
from dynmap_timelapse import timelapse_dynmap
from make_movie import make_mp4
import schedule
import shutil

mp4_dir = "./dynmap_mp4"
img_dir = "./images"
CK = ""
CS = ""
AT = ""
AS = ""

api = twitter.Api(consumer_key=CK,
                  consumer_secret=CS,
                  access_token_key=AT,
                  access_token_secret=AS
                  )


def waiting(func):
    def wrapper(obj, *args, **kwargs):
        time.sleep(5)
        return func(obj, *args, **kwargs)

    return wrapper


def tweet_mp4():
    now = datetime.datetime.now()
    movie = mp4_dir + "/movie.mp4"  # 画像を投稿するなら画像のパス

    if datetime.date.today().weekday() == 4:
        make_mp4(img_dir+"/*", movie)
        shutil.rmtree(img_dir)
        os.mkdir(img_dir)
    else:
        yesterday = now - datetime.timedelta(days=1)
        make_mp4(img_dir+"/{0:%Y%m%d}".format(yesterday), movie)
    org = api._RequestUrl
    api._RequestUrl = waiting(org)
    api.PostUpdate(status="アルカディア鯖整地1タイムラプス", media=movie, media_category="tweet_video")
    api._RequestUrl = org


if __name__ == '__main__':
    # 動画付きツイート
    if not os.path.exists(mp4_dir):
        os.mkdir(mp4_dir)
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    schedule.every(10).minutes.do(timelapse_dynmap)
    schedule.every().day.at("0:00").do(tweet_mp4)

    tweet_mp4()

    while True:
        schedule.run_pending()
        time.sleep(60)
