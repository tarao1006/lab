import subprocess
import cv2
import tqdm


if __name__ == "__main__":
    sim_num = 7

    a0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/020/fixed.png')
    b0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/030/fixed.png')
    c0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/040/fixed.png')
    d0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/050/fixed.png')
    e0 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/00/060/fixed.png')

    a1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/020/fixed.png')
    b1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/030/fixed.png')
    c1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/040/fixed.png')
    d1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/050/fixed.png')
    e1 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/01/060/fixed.png')

    a2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/020/fixed.png')
    b2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/030/fixed.png')
    c2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/040/fixed.png')
    d2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/050/fixed.png')
    e2 = cv2.imread(f'/Users/taiga/Projects/lab/simulation/sim{sim_num:0=2.0f}/figs/02/060/fixed.png')

    hcon0 = cv2.hconcat([a0, b0, c0, d0, e0])
    hcon1 = cv2.hconcat([a1, b1, c1, d1, e1])
    hcon2 = cv2.hconcat([a2, b2, c2, d2, e2])
    finish = cv2.vconcat([hcon0, hcon1, hcon2])
    cv2.imwrite(f'../figs/sim{sim_num:0=2.0f}/fixed.png', finish)
