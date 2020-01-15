import os
import shutil
import numpy as np
from pathlib import Path
from pyudf import Udf
from pyudf.rotation import z_rotation

udf = Udf()
udf.load_jsonconfig()

q = z_rotation(17 * 2 * np.pi / 32)
udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q0'] = q.q0
udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q1'] = q.q1
udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q2'] = q.q2
udf.data['switch']['init_distribution']['user_specify']['particles'][0]['q']['q3'] = q.q3

_shearrates = np.linspace(0.01, 0.1, 10)

if not Path('udf').exists():
    os.mkdir('udf')

for i, s in enumerate(_shearrates):
    udf.data['constitutive_eq']['shear_navier_stokes']['external_field']['dc']['shear_rate'] = s
    os.mkdir(f'udf/{i:0=2.0f}')
    udf.to_udf(f'udf/{i:0=2.0f}/input.udf')
    shutil.copy('/Users/taiga/Projects/lab/simulation/define.udf', f'udf/{i:0=2.0f}/')
