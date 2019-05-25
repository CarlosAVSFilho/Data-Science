import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt

# Relembrando
base = pd.read_csv('trees.csv')
srn.distplot(base.Volume, bins = 10, axlabel = 'Volume').set_title('Árvores')

#Novo plot
base2 = pd.read_csv('chicken.csv')

agrupado = base2.groupby(['feed'])['weight'].sum()

teste = base2.loc[base2['feed'] == 'horsebean']

plt.figure()
plt.subplot(3,2,1)
srn.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist = True).set_title('horsebean')

plt.subplot(3,2,2)
srn.distplot(base2.loc[base2['feed'] == 'casein'].weight, hist = True).set_title('casein')

plt.subplot(3,2,3)
srn.distplot(base2.loc[base2['feed'] == 'linseed'].weight, hist = True).set_title('linseed')

plt.subplot(3,2,4)
srn.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight, hist = True).set_title('meatmeal')

plt.subplot(3,2,5)
srn.distplot(base2.loc[base2['feed'] == 'soybean'].weight, hist = True).set_title('soybean')

plt.subplot(3,2,6)
srn.distplot(base2.loc[base2['feed'] == 'sunflower'].weight, hist = True).set_title('sunflower')

plt.tight_layout()