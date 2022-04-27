import pandas as pd
import numpy as np

def split(n_phase):
    all = pd.read_csv('adult.all', ',')
    phases = np.array_split(all, n_phase)
    for i in range(n_phase):
        phases[i].to_csv('phase_{}'.format(i + 1), index=False)

if __name__ == '__main__':
    split(8)