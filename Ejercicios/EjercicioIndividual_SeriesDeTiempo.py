# Talento TICs 2023
# Pyton 2

# Relacionando dos datasets
# Concatenacion y merge de dataset
import pandas as pd
import matplotlib.pyplot as plt

df_data1 = pd.read_csv('Ejercicios/sampleDatasets/ds1.csv')
df_data2 = pd.read_csv('Ejercicios/sampleDatasets/ds1_pt2.csv')

print(df_data1)
print(df_data2)

# El merge, mezcla dos dataset, dataframe a partir de una columna comun;
# No importa que tengan distinto # de filas
df_all_data = pd.merge(df_data1, df_data2, on = "TIEMPO")

df_group = df_all_data.groupby("TIEMPO")["EST. LACIUDADELA PM10"].mean().plot(kind="bar")
plt.show()
print(df_all_data)