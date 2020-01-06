import re
import glob
import subprocess

import cv2

PATTERN = re.compile(r'^[^_]*.jpg$')


def crop_center(img, cw, ch):
    h, w, _ = img.shape
    return img[
        (h - ch) // 2:(h + ch) // 2,
        (w - cw) // 2:(w + cw) // 2,
        :
    ]


def triming_img():
    imgs = [img for img in glob.glob('*.jpg') if PATTERN.match(img)]
    imgs.sort()
    for i, img in enumerate(imgs):
        imgarray = cv2.imread(img)
        cv2.imwrite(f'_{i:0=3.0f}.jpg', crop_center(imgarray, 460, 460))


if __name__ == "__main__":
    triming_img()
    subprocess.run(['ffmpeg', '-f', 'image2', '-r', '15', '-i', '_%03d.jpg', '-r', '15', '-an', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', 'video.mp4'])
