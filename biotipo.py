import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("dados_biotipo.csv")

#Primeiro devemos transformar os dados de peso e altura em numéricos, pois eles estão sendo lidos como strings
df['Peso'] = pd.to_numeric(df['Peso'], errors='coerce')
df['Altura'] = pd.to_numeric(df['Altura'], errors='coerce')

#Agora descobriremos a média do peso, a mediana da altura e as modas de cor de cabelo e cor de olho
print('Média: Peso = ', df['Peso'].mean())
print('Mediana: Altura = ', df['Altura'].median())
print('Moda: Cor Olho = ', df['Cor Olho'].mode())
print('Moda: Cor Cabelo = ', df['Cor Cabelo'].mode())

#Agora substituiremos os valores faltantes de cada coluna pelos valores previamente mencionados
df['Peso']= df['Peso'].replace(np.nan, df['Peso'].mean())
df['Altura']= df['Altura'].replace(np.nan, df['Altura'].median())     
df['Cor Cabelo']=df['Cor Cabelo'].replace(' ', df['Cor Cabelo'].mode())
df['Cor Olho']=df['Cor Olho'].replace(' ', df['Cor Olho'].mode())
df.info()

#Por fim, identificamos outliers na coluna IMC usando o zscore
zscorearray = np.abs(stats.zscore(df['IMC']))
for i in range (len(zscorearray)):
    if zscorearray[i] > 3:
        print('IMC Outlier detectado: entrada {}, IMC {}, zscore {:.2f}'.format(i, df['IMC'][i], zscorearray[i]))

