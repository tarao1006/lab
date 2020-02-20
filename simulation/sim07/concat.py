import subprocess
import cv2
import tqdm


if __name__ == "__main__":
    sim_num = 7

    for i in tqdm.tqdm(range(401)):
        a0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/00/020/_{i:0=3.0f}.png')
        b0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/00/030/_{i:0=3.0f}.png')
        c0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/00/040/_{i:0=3.0f}.png')
        d0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/00/050/_{i:0=3.0f}.png')
        e0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/00/060/_{i:0=3.0f}.png')

        a1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/01/020/_{i:0=3.0f}.png')
        b1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/01/030/_{i:0=3.0f}.png')
        c1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/01/040/_{i:0=3.0f}.png')
        d1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/01/050/_{i:0=3.0f}.png')
        e1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/01/060/_{i:0=3.0f}.png')

        a2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/02/020/_{i:0=3.0f}.png')
        b2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/02/030/_{i:0=3.0f}.png')
        c2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/02/040/_{i:0=3.0f}.png')
        d2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/02/050/_{i:0=3.0f}.png')
        e2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/figs/sim{sim_num:0=2.0f}/figs4movies/02/060/_{i:0=3.0f}.png')

        hcon0 = cv2.hconcat([a0, b0, c0, d0, e0])
        hcon1 = cv2.hconcat([a1, b1, c1, d1, e1])
        hcon2 = cv2.hconcat([a2, b2, c2, d2, e2])
        finish = cv2.vconcat([hcon0, hcon1, hcon2])
        cv2.imwrite(f'../figs/sim{sim_num:0=2.0f}/figs4movies/_{i:0=3.0f}.png', finish)

    subprocess.run(['ffmpeg', '-f', 'image2', '-r', '15', '-i', f'../figs/sim{sim_num:0=2.0f}/figs4movies/_%03d.png', '-r', '15', '-an', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', f'../figs/sim{sim_num:0=2.0f}/_video.mp4'])
