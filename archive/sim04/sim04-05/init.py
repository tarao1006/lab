import os
import shutil
import numpy as np
from traitlets.config import JSONFileConfigLoader
from pyudf import Udf

import sys
sys.path.append('/Users/taiga/Projects/lab/simulation/utils')
from rotation import shift_phases, z_rotation

udf = Udf()
with JSONFileConfigLoader('define.json') as c:
    udf.update_config(c)

degree = shift_phases([0])
q = z_rotation(degree[0])


udf.constitutive_eq['shear_navier_stokes']['external_field']['dc']['shear_rate'] = 0.10
udf.switch['init_distribution']['user_specify']['particles'][0]['q']['q0'] = q.q0
udf.switch['init_distribution']['user_specify']['particles'][0]['q']['q1'] = q.q1
udf.switch['init_distribution']['user_specify']['particles'][0]['q']['q2'] = q.q2
udf.switch['init_distribution']['user_specify']['particles'][0]['q']['q3'] = q.q3


for i, v in enumerate([0.0, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]):
    udf.object_type['spherical_particle']['particle_specs'][0]['janus_slip_vel'] = v
    if i == 0:
        udf.object_type['spherical_particle']['particle_specs'][0]['janus_populsion'] = 'OFF'
    else:
        udf.object_type['spherical_particle']['particle_specs'][0]['janus_populsion'] = 'SQUIRMER'

    os.mkdir(f'udf/{v*100:0=3.0f}')
    udf.create_input_file(f'udf/{v*100:0=3.0f}/input.udf')
    shutil.copy('/Users/taiga/Projects/lab/simulation/sim00/define.udf', f'udf/{v*100:0=3.0f}/')
