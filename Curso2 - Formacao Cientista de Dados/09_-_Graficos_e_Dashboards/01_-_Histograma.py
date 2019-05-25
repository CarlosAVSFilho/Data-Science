import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base = pd.read_csv('trees.csv')
base.head()
h = np.histogram(base.iloc[:,1], bins = 2)

plt.hist(base.iloc[:,1], bins = 6)
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')
