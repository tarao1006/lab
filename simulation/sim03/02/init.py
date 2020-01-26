import os
import shutil
import numpy as np
from pathlib import Path
from pyudf import Udf

udf = Udf()
udf.load_jsonconfig()
udf.data['object_type']['spherical_particle']['particle_spec'][0]['janus_slip_vel'] = 0.01
udf.data['object_type']['spherical_particle']['particle_spec'][0]['janus_slip_mode'] = -50.0
udf.data['gravity']['g'] = 0.06

gammadots = np.arange(0.0, 0.105, 0.005)

if not Path(f'udf').exists():
    os.mkdir(f'udf')

for gammadot in gammadots:
    gammadot_str = f'{gammadot * 1000:0=3.0f}'
    udf.data['constitutive_eq']['shear_navier_stokes']['external_field']['dc']['shear_rate'] = gammadot

    os.mkdir(f'udf/{gammadot_str}')
    udf.to_udf(f'udf/{gammadot_str}/input.udf')
    shutil.copy('/Users/taiga/Projects/lab/simulation/define.udf', f'udf/{gammadot_str}')
