import subprocess
import cv2
import tqdm


if __name__ == "__main__":
    sim_num = 5

    for i in tqdm.tqdm(range(401)):
        a0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/udf/020/{i:0=3.0f}.png')
        b0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/udf/030/{i:0=3.0f}.png')
        c0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/udf/040/{i:0=3.0f}.png')
        d0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/udf/050/{i:0=3.0f}.png')
        e0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/udf/060/{i:0=3.0f}.png')

        a1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/udf/020/{i:0=3.0f}.png')
        b1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/udf/030/{i:0=3.0f}.png')
        c1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/udf/040/{i:0=3.0f}.png')
        d1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/udf/050/{i:0=3.0f}.png')
        e1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/udf/060/{i:0=3.0f}.png')

        a2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/udf/020/{i:0=3.0f}.png')
        b2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/udf/030/{i:0=3.0f}.png')
        c2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/udf/040/{i:0=3.0f}.png')
        d2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/udf/050/{i:0=3.0f}.png')
        e2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/udf/060/{i:0=3.0f}.png')

        hcon0 = cv2.hconcat([a0, b0, c0, d0, e0])
        hcon1 = cv2.hconcat([a1, b1, c1, d1, e1])
        hcon2 = cv2.hconcat([a2, b2, c2, d2, e2])
        finish = cv2.vconcat([hcon0, hcon1, hcon2])
        cv2.imwrite(f'figs/sim{sim_num:0=2.0f}/figs4movies/_{i:0=3.0f}.png', finish)

    subprocess.run(['ffmpeg', '-f', 'image2', '-r', '15', '-i', f'figs/sim{sim_num:0=2.0f}/figs4movies/_%03d.png', '-r', '15', '-an', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', 'video.mp4'])