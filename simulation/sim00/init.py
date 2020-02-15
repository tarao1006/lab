import os
import shutil
import numpy as np
from pathlib import Path
from pyudf import Udf
from pyudf.rotation import z_rotation

udf = Udf()
udf.load_jsonconfig()

_degrees = [d * 2 * np.pi / 32 for d in range(1, 33)]
_degrees_str = [f'{i:0=2}' for i in range(1, 33)]

if not Path('udf').exists():
    os.mkdir('udf')

for d, d_str in zip(_degrees, _degrees_str):
    q = z_rotation(d)
    udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q0'] = q.q0
    udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q1'] = q.q1
    udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q2'] = q.q2
    udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q3'] = q.q3

    os.mkdir(f'udf/{d_str}')
    udf.to_udf(f'udf/{d_str}/input.udf')
    shutil.copy('/Users/taiga/Projects/lab/simulation/define.udf', f'udf/{d_str}/')
