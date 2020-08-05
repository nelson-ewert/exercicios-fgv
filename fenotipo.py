import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dados_fenotipo.csv")

df.info()
print('Média: Peso = ', df['Peso'].mean())
print('Média: Altura = ', df['Altura'].mean())
print('Mediana: Peso = ', df['Peso'].median())
print('Mediana: Altura = ', df['Altura'].median())
print('1o quartil: Peso = ', df['Peso'].quantile(q=0.25))
print('1o quartil: Altura = ', df['Altura'].quantile(q=0.25))
print('3o quartil: Peso = ', df['Peso'].quantile(q=0.75))
print('3o quartil: Altura = ', df['Altura'].quantile(q=0.75))
print('Desvio Padrão: Peso = ', df['Peso'].std())
print('Desvio Padrão: Altura = ', df['Altura'].std())

print(pd.pivot_table(df,index=["Cor Olho", "Cor Cabelo"], aggfunc='count', margins=True))

plt.scatter(df['Peso'],df['Altura'])
plt.show()
