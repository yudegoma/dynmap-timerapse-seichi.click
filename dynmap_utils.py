#!/usr/bin/env python
import cv2
import numpy as np


def pil_to_cv2(pil_img):
    cv2im = np.asarray(pil_img)
    return cv2.cvtColor(cv2im, cv2.COLOR_BGR2RGB)


# 画像の切り取り
def crop(img: np.ndarray) -> np.ndarray:
    img_mask = np.where(img == 0, 255, 0)
    img_mask = img_mask[:, :, 2]

    H, W = img_mask.shape
    c_x = W // 2
    c_y = H //2
    x1 = W // 2
    y1 = H // 2
    x2 = W // 2
    y2 = H // 2

    # left
    for x in range(c_x//2, 0, -1):
        x1 = x
        if img_mask[c_y, x] == 255 or img_mask[c_y + 64, x] == 255 or img_mask[c_y - 64, x] == 255:
            break

    # right
    for x in range(c_x+c_x//2, W):
        x2 = x
        if img_mask[c_y, x] == 255 or img_mask[c_y + 64, x] == 255 or img_mask[c_y - 64, x] == 255:
            break

    # top
    for y in range(c_y//2, 0, -1):
        y1 = y
        if img_mask[y, c_x] == 255 or img_mask[y, c_x + 64] == 255 or img_mask[y, c_x - 64] == 255:
            break

    # bottom
    for y in range(c_y+c_y//2, H):
        y2 = y
        if img_mask[y, c_x] == 255 or img_mask[y, c_x + 64] == 255 or img_mask[y, c_x - 64] == 255:
            break

    crop_img = img[y1+1:y2, x1+1:x2]

    return crop_img

