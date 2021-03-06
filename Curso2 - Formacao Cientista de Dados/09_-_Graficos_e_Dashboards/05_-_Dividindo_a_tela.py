import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('trees.csv')

plt.figure(1)

# Girth x Volume
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)

# Girth x Height
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)

# Height x Volume
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume)

# Histograma x Volume
plt.subplot(2,2,4)
plt.hist(base.Volume)