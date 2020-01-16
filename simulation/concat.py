import numpy as np
import subprocess


a = {round(i, 5) : f"sim09/sim09-00/udf/{j:0=2.0f}" for j, i in enumerate(np.linspace(0.01, 0.1, 10))}
b = {round(i, 5) : f"sim10/sim10-00/udf/{j:0=2.0f}" for j, i in enumerate(np.linspace(0.04, 0.06, 10))}
c = {round(i, 5) : f"sim10/sim10-01/udf/{j:0=2.0f}" for j, i in enumerate(np.linspace(0.02, 0.04, 10))}
a.update(b)
a.update(c)

aa = sorted(a.items(), key=lambda x:x[0])
print(aa)
for i, a in enumerate(aa):
    subprocess.check_output(f'cp -r {a[1]} sim11/{i:0=3.0f}', shell=True)
