""" 1. Carga
    2. Limpieza / correccion
    3. seleccion de columnas / filas
    4. Factorizacion ( para analisis de correlacion)
"""
import pandas as pd

# Se carga el dataframe: 
df_Drink_1 = pd.read_csv('Ejercicios/sampleDatasets/drinks.csv')
df_Drink_1.info()

#Se seleccionan las siguientes columnas: 
df_Dr1 = df_Drink_1 [["wine_servings","spirit_servings","beer_servings"]]
print(df_Dr1.corr())

#Se realiza la factorizacion:
df_Drink_1 = df_Drink_1.apply(lambda x: pd.factorize(x)[0])
print(df_Drink_1.corr())