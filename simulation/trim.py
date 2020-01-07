import re
import sys
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


def triming_img(prefix):
    imgs = [img for img in glob.glob(f'{prefix}/*.jpg') if PATTERN.match(img)]
    imgs.sort()
    for i, img in enumerate(imgs):
        imgarray = cv2.imread(img)
        cv2.imwrite(f'{prefix}/_{i:0=3.0f}.jpg', crop_center(imgarray, 460, 460))


if __name__ == "__main__":
    try:
        sim_num = int(sys.argv[1])
    except IndexError:
        raise IndexError('sim_num must be selected.')
    except ValueError:
        raise ValueError('sim_num must be int.')
    try:
        sub_sim_num = int(sys.argv[2])
    except IndexError:
        sub_sim_num = None
    except ValueError:
        raise ValueError('sub_sim_num must be int.')

    prefix = f'/Users/taiga/Projects/lab/simluation/sim{sim_num:0=2.0f}/ImageCapture/output.udf/graphic'
    if sub_sim_num is not None:
        prefix = f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/udf/{sub_sim_num:0=2.0f}/ImageCapture/output.udf/graphic'
    triming_img(prefix)
    subprocess.run(['ffmpeg', '-f', 'image2', '-r', '15', '-i', f'{prefix}/_%03d.jpg', '-r', '15', '-an', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', f'{sim_num:0=2.0f}_{sub_sim_num:0=3.0f}_video.mp4'])
