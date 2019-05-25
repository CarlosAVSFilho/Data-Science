import pandas as pd

base = pd.read_csv('insect.csv')

agrupado = base.groupby(['spray'])['count'].sum()

# Gráfico de barras
agrupado.plot.bar()#color = 'gray'

# Gráfico de setores
agrupado.plot.pie(legend = True)
