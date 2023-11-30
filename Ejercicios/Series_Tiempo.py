""" EJERCICIO EN CLASE: DATASET CON SERIE DE TIEMPO. CRIMINALIDAD BALTIMORE, US

0. Cargar el dataset
1. Crear una nueva columna datetime : CrimeDate, Crimetime
2. Formateat columna datatime
3. Crear tabla pivote """

import pandas as pd
import matplotlib.pyplot as plt

#carga del dataset:
df_BCdata_temp = pd.read_csv('Ejercicios/sampleDatasets/BaltimoreCrimeData.csv',parse_dates=["CrimeDate", "CrimeTime"])

#adecuación del dataset para manejo de datos temporales:
print(f"dataset sin limpiar:{df_BCdata_temp.info()}")