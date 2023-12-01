import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

df_cod_medic = pd.read_csv('Ejercicios/sampleDatasets/CODIGO_MEDICAMENTOS_VIGENTES.csv')


print(df_cod_medic.info())

df_crimes_sub = df_cod_medic[ ["CrimeDate","CrimeTime","Total Incidents","Neighborhood","Description","Location","District"]  ]

df_crimes_sub = df_crimes_sub.dropna()
df_crimes_sub.info()


#Convertir a una tabla pivote (donde se construya el índice de la tabla a partir de la info temporal):
# pivot_table permite valores duplicados a partir del índice:
# pivot no permite valores duplicados
df_crimes_pivot = df_crimes_sub.pivot_table(index=["datetime"], columns=["District"],values="Total Incidents",aggfunc="sum",fill_value=0)



print(df_crimes_pivot.head(100))

#continura el ejercicio...

#agrupamientos y agregaciones para visualización


#visualización de datos muestreados en una frecuencia distinta
fig, axes=plt.subplots(1,2)
df_crimes_pivot.resample("M").sum().plot(kind="bar",ax=axes[0], rot=0)
df_crimes_pivot.resample("W").sum().plot(kind="bar",ax=axes[1], rot=0)
plt.show()