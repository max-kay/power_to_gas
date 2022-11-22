import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from utils import convert_time_gas, convert_time_ms, compare_ms_gas


# read data
start_ms = datetime.fromisoformat('2022-11-15 13:59:40')
ms = convert_time_ms(pd.read_csv('data/ms/h2_pulses.csv',
                     header=20), start_time=start_ms, t0=start_ms)
print(ms.describe())

gas5 = convert_time_gas(pd.read_csv(
    './data/gas/h2_pulse_5bar.csv', header=4, sep='\t'), start_ms)
print(gas5.describe())

gas10 = convert_time_gas(pd.read_csv(
    './data/gas/h2_pulse_10bar.csv', header=4, sep='\t'), start_ms)
print(gas10.describe())


start5 = 154
end5 = 1160

start10 = 2169
end10 = 3132

# make figure
# fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, sharex=True)

# # plot ms
# ax1.plot(ms['Time'], ms['Hydrogen'])
# ax1.axvline(start5, color='r')
# ax1.axvline(end5, color='r')

# ax1.axvline(start10, color='y')
# ax1.axvline(end10, color='y')

# # plot gas5
# ax2.plot(gas5['Time'], gas5['MFC1 PV [ml/min]'], color='r')
# ax3.plot(gas5['Time'], gas5['P PV [bar]'], color='r')

# # plot gas10
# ax4.plot(gas10['Time'], gas10['MFC1 PV [ml/min]'], color='y')
# ax5.plot(gas10['Time'], gas10['P PV [bar]'], color='y')
# ax6.plot(gas10['Time'], gas10['P SP [bar]'], color='y')

# plt.show()


# figure for 5bar pulse
compare_ms_gas(ms, gas5, 'MFC1 PV [ml/min]',
               '5 bar Puls mit Wasserstoff', start5, end5)

# figure for 10bar pulse
compare_ms_gas(ms, gas10, 'MFC1 PV [ml/min]',
               '10 bar Puls mit Wasserstoff', start10, end10)

