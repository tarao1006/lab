import pandas as pd
import re


def create_csv(text_file):
    """
    """
    header = 'time,shear_rate_temporal,shear_strain_temporal,shear_stress_temporal,viscosity'
    parent = text_file.parent

    with (parent / 'output.csv').open(mode='w') as g:
        g.write(header + '\n')
        with text_file.open(mode='r') as f:
            for line in f:
                if line.startswith(' '):
                    g.write(re.sub(r'\s+', ',', line)[1:-1] + '\n')


def gather_csv(csv_files):
    """
    """
    all_contents = pd.DataFrame(columns=['time', 'shear_rate_temporal', 'shear_strain_temporal', 'shear_stress_temporal', 'viscosity'])
    parent = csv_files[0].parent.parent

    for csv_file in csv_files:
        contents = pd.read_csv(csv_file)
        all_contents = pd.concat([all_contents, contents.tail(1)])

    all_contents = all_contents.reset_index(drop=True)
    all_contents = all_contents.drop('time', axis=1)
    all_contents.to_csv(f'{parent}/all_data.csv', index=False)
