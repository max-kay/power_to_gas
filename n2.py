import pandas as pd
from utils import compare_ms_gas_n2, convert_time_gas, convert_time_ms
from datetime import datetime

start_ms = datetime.fromisoformat('2022-11-15 10:55:13')
ms = convert_time_ms(pd.read_csv('./data/ms/n2.csv', header=20), start_ms, start_ms)
gs = convert_time_gas(pd.read_csv('./data/gas/n2.csv', header=4, sep='\t'), start_ms)

compare_ms_gas_n2(ms, gs, 'MFC2 PV [ml/min]', 'Variabler Druck mit N2', 1927, 2306)
