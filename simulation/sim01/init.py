import os
import shutil
from pathlib import Path
from pyudf import Udf

udf = Udf()
udf.load_jsonconfig()

gammadots = [0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
B1s = [0.00, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]


for gammadot in gammadots:
    gammadot_str = f'{gammadot * 100:0=3.0f}'
    udf.data['constitutive_eq']['shear_navier_stokes']['external_field']['dc']['shear_rate'] = gammadot

    if not Path(f'gammadot/{gammadot_str}/B1').exists():
        os.mkdir(f'gammadot/{gammadot_str}/B1')

    for B1 in B1s:
        B1_str = f'{B1 * 100:0=3.0f}'
        if B1_str == '000':
            udf.data['object_type']['spherical_particle']['particle_spec'][0]['janus_propulsion'] = 'OFF'
        else:
            udf.data['object_type']['spherical_particle']['particle_spec'][0]['janus_propulsion'] = 'SQUIRMER'
            udf.data['object_type']['spherical_particle']['particle_spec'][0]['janus_slip_vel'] = B1

        os.mkdir(f'gammadot/{gammadot_str}/B1/{B1_str}')
        udf.to_udf(f'gammadot/{gammadot_str}/B1/{B1_str}/input.udf')
        shutil.copy('/Users/taiga/Projects/lab/simulation/define.udf', f'gammadot/{gammadot_str}/B1/{B1_str}/')
