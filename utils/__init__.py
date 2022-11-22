import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

def convert_time_ms(df: pd.DataFrame, start_time: dt.datetime, t0: dt.datetime) -> pd.DataFrame:
    ts = df['Time(s)']
    new_ts = []
    for t in ts:
        new_ts.append((start_time + dt.timedelta(seconds=t) -t0).total_seconds())
    new_ts = np.array(new_ts)
    del df['Time(s)']
    df['Time'] = new_ts
    return df

def convert_time_gas(df: pd.DataFrame, t0: dt.datetime) -> pd.DataFrame:
    ts = df['Time']
    new_ts = []
    for t in ts:
        new_ts.append((dt.datetime.fromisoformat('2022-11-15 '+t) - t0).total_seconds())
        
    new_ts = np.array(new_ts)
    del df['Time']
    del df['Date']
    df['Time'] = new_ts
    return df


def compare_ms_gas(ms_frame: pd.DataFrame, gas_frame: pd.DataFrame, gas_channel: str, title: str, start, end):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    
    selected_ms = ms_frame[(ms_frame.Time > start) & (ms_frame.Time < end)]
    selected_gas = gas_frame[(gas_frame.Time > start) & (gas_frame.Time < end)]

    ax1.plot(selected_ms['Time'], selected_ms['Hydrogen'])
    ax1.set_ylabel('Häufigkeit [Torr]')
    
    ax2.plot(selected_gas['Time'], selected_gas[gas_channel])
    ax2.set_ylabel('Wasserstofffluss [ml/min]')

    ax3.plot(selected_gas['Time'], selected_gas['P PV [bar]'])
    ax3.set_ylabel('Druck [bar]')
    ax3.set_xlabel('Zeit [s]')

    ax1.set_title(title)


    fig.set_size_inches(6.4, 6.4)
    fig.tight_layout()
    fig.savefig(f'./out/{title}.png', dpi=300, bbox_inches='tight')


def compare_ms_gas_n2(ms_frame: pd.DataFrame, gas_frame: pd.DataFrame, gas_channel: str, title: str, start, end):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    selected_ms = ms_frame[(ms_frame.Time > start) & (ms_frame.Time < end)]
    selected_gas = gas_frame[(gas_frame.Time > start) & (gas_frame.Time < end)]

    ax1.plot(selected_ms['Time'], selected_ms['Nitrogen'])
    ax1.set_ylabel('Häufigkeit [Torr]')

    ax2.plot(selected_gas['Time'], selected_gas[gas_channel])
    ax2.set_ylabel('Stickstofffluss [ml/min]')

    ax3.plot(selected_gas['Time'], selected_gas['P PV [bar]'])
    ax3.set_ylabel('Druck [bar]')
    ax3.set_xlabel('Zeit [s]')

    ax1.set_title(title)
    fig.set_size_inches(6.4, 6.4)
    fig.tight_layout()
    fig.savefig(f'./out/{title}.png', dpi=300, bbox_inches='tight')
