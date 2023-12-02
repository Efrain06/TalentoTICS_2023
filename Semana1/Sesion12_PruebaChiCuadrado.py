# Talento TICs 2023
# Python para analisis de datos

# Prueba de chi-cuadrado : prueba que determina la dependencia entre dos variales
# categoricas en una muesra de datos. Se realiza dobre una tabla de contingencia,
# analisando las frecuencias de las variables.


# Tabla de contingencia: Resume la frecuencias de unas variables categoricas

import pandas as pd
from scipy.stats import chi2_contingency

data = {
    "Ciudad" :["Cali", "Cali", "Medellin", "Bogota", "Barranquilla", "B/manga", "Cartagena", "Cucuta", "Pereira", "Manizales", "Pasto"],
    "Genero": ["Salsa", "Rock", "Reggaeton", "Salsa", "Salsa", "Reggaeton", "Champeta", "Salsa", "Tropipop", "Tango", "Vallenatos"]

}

df_generos = pd.DataFrame(data)
print(df_generos)

tb_cont = pd.crosstab(df_generos["Ciudad"], df_generos["Genero"])
tb_cont_tl = pd.crosstab(df_generos["Ciudad"], df_generos["Genero"], margins=True, margins_name="Total")

print(tb_cont)
print(tb_cont_tl)


# Prueba de chi-cuadrado sobre la tabla de contingencia (Frecuencia de datos categoricos)

chi2, p,a,b = chi2_contingency(tb_cont)
print(f"Parametro de chi 2:{chi2}")
print(f"Parametro de p:{p}")

alpha = 0.005 # Nivel de significancia de la prueba

if p < alpha:
    print("La prueba es significativa")
else:
    print("La prueba NO es significativa")


   