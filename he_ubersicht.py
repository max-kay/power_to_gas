import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/ms/he_ubersicht.csv', header=19)

print(df.describe())
plt.plot(df['A'], df['B'])
plt.title('Massenspektrograph zum Start des Helium Versuchs')
plt.yscale('log')
plt.xlabel('m/z')
plt.ylabel('Häufigkeit [Torr]')
plt.savefig('./out/he_ubersicht.png', dpi = 300, bbox_inches='tight')
