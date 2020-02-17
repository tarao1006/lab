import re
import sys
import glob
import subprocess
import tqdm

import cv2

PATTERN = re.compile(r'^[^_]*.jpg$')


def crop_center(img, cw, ch):
    h, w, _ = img.shape
    return img[
        (h - ch) // 2:(h + ch) // 2,
        (w - cw) // 2:(w + cw) // 2,
        :
    ]


def triming_img(prefix):
    imgs = [img for img in glob.glob(f'{prefix}/*.jpg') if PATTERN.match(img)]
    imgs.sort()
    for i, img in tqdm.tqdm(enumerate(imgs)):
        imgarray = cv2.imread(img)
        cv2.imwrite(f'{prefix}/_{i:0=3.0f}.jpg', crop_center(imgarray, 300, 400))


if __name__ == "__main__":
    sim_num = 5
    for i in [2]:  # range(0, 3):
        sub_sim_num = i
        for j in ['030']:  # ['020', '030', '040', '050', '060']:
            prefix = f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/{sub_sim_num:0=2.0f}/udf/{j}/output/output.udf/graphic'
            triming_img(prefix)
        # subprocess.run(['ffmpeg', '-f', 'image2', '-r', '15', '-i', f'{prefix}/_%03d.jpg', '-r', '15', '-an', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', f'{sim_num:0=2.0f}_{sub_sim_num:0=3.0f}_video.mp4'])
