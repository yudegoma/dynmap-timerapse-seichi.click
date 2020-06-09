from glob import glob
import datetime
import os
import sys
import imageio
import cv2

gif_dir = "./dynmap_gif/"
now = datetime.datetime.now()

# 画像劣化を起こさずgifファイルを作成
def make_gif(img_dir: str):
    if os.path.exists(img_dir):
        files = sorted(glob(img_dir + "/*"))
    else:
        sys.exit(0)

    if not os.path.exists(gif_dir):
        os.mkdir(gif_dir)

    images = []
    for f in files:
        img = cv2.imread(f)
        img = cv2.resize(img, (512, 512))
        images.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    imageio.mimsave(gif_dir + '{0:%Y%m%d}.gif'.format(now), images, duration=0.7)


if __name__ == '__main__':
    make_gif("./{0:%Y%m%d}".format(now))
