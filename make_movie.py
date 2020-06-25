#!/usr/bin/env python
from glob import glob
import cv2
import imageio

import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

def make_mp4(img_dir, out_file, fps):
    # encoder(for mp4)

    files = sorted(glob(img_dir + "/*.png", recursive=True))
    writer = imageio.get_writer(out_file, fps=fps)

    for f in files:
        # hoge0000.png, hoge0001.png,..., hoge0090.png
        img = cv2.imread(f)
        img = cv2.resize(img, (512, 512))
        text = f.split(".")[1].split("_")[2]
        cv2.putText(img, text, (0, 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1, cv2.LINE_AA)
        # add
        writer.append_data(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    writer.close()