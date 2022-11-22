from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from utils import convert_time_gas


start = datetime.fromisoformat('2022-11-15 16:16:30')

df = pd.read_csv('./data/gas/sieverts_h2.csv', header=5, sep='\t')
sieverts = convert_time_gas(df, start)

print(sieverts.describe())

# volume determination
max_perssure_idx = sieverts.idxmax()['P PV [bar]']
flows = sieverts['MFC1 SP [ml/min]'][:max_perssure_idx]
times = sieverts['Time'][:max_perssure_idx]

under_pressure_vol = 0

for i in range(1, max_perssure_idx):
    under_pressure_vol += flows[i] / 60 * (times[i] - times[i-1])

standart_pressure = 100_000

max_pressure = sieverts['P PV [bar]'][max_perssure_idx] * 100_000
vol = standart_pressure/max_pressure * under_pressure_vol

# selected sieverts for flux analsis
sel_sieverts = sieverts[(sieverts.Time > 635) & (sieverts.Time < 2273)]

slope, intercept, _, _, _ = linregress(
    sel_sieverts['Time'],  sel_sieverts['P PV [bar]'])
slope *= 100_000

R = 8.3145
temperature = sieverts.mean()['ET PV [�C]'] + 273.15

thickness = 0.12/1000
area = 0.012*0.012*3.14159263538


permeability = -slope * vol/R/temperature/area * thickness/max_pressure
print('He')
print('dp/dt: ', slope)
print('volume: ', vol)
print('permeability: ', permeability)

exit()

fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(sel_sieverts['Time'], sel_sieverts['P PV [bar]'])
ax1.set_ylabel('messwert')
ax2.plot(sel_sieverts['Time'], sel_sieverts['P SP [bar]'])
ax2.set_ylabel('sollwert')
plt.show()
