import subprocess
import cv2
import tqdm


if __name__ == "__main__":
    sim_num = 6

    for i in tqdm.tqdm(range(401)):
        a0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/00/udf/020/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        b0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/00/udf/030/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        c0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/00/udf/040/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        d0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/00/udf/050/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        e0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/00/udf/060/output/output.udf/graphic/_{i:0=3.0f}.jpg')

        a1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/01/udf/020/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        b1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/01/udf/030/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        c1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/01/udf/040/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        d1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/01/udf/050/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        e1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/01/udf/060/output/output.udf/graphic/_{i:0=3.0f}.jpg')

        a2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/02/udf/020/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        b2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/02/udf/030/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        c2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/02/udf/040/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        d2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/02/udf/050/output/output.udf/graphic/_{i:0=3.0f}.jpg')
        e2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/02/udf/060/output/output.udf/graphic/_{i:0=3.0f}.jpg')

        hcon0 = cv2.hconcat([a0, b0, c0, d0, e0])
        hcon1 = cv2.hconcat([a1, b1, c1, d1, e1])
        hcon2 = cv2.hconcat([a2, b2, c2, d2, e2])
        finish = cv2.vconcat([hcon0, hcon1, hcon2])
        cv2.imwrite(f'figs/sim{sim_num:0=2.0f}/figs4movies/_{i:0=3.0f}.jpg', finish)

    subprocess.run(['ffmpeg', '-f', 'image2', '-r', '15', '-i', f'figs/sim{sim_num:0=2.0f}/figs4movies/_%03d.jpg', '-r', '15', '-an', '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', 'video.mp4'])
