import pandas as pd
from utils import compare_ms_gas, convert_time_gas, convert_time_ms
from datetime import datetime

# missing data

start_ms = datetime.fromisoformat('2022-11-15 10:55:13')
ms = convert_time_ms(pd.read_csv('./data/ms/h2.csv',
                     header=20), start_ms, start_ms)
gs = convert_time_gas(pd.read_csv(
    './data/gas/h2.csv', header=4, sep='\t'), start_ms)

compare_ms_gas(ms, gs, 'MFC2 PV [ml/min]',
                  'steigender Druck mit Wasserstoff', 0, 40000)
print(ms.describe())
print(gs.describe())
