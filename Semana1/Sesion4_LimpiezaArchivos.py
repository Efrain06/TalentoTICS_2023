#Talento TICs 2023 - Python 2 (python para analítica de datos)
# Sesión 4 - Limpieza de dataframes (Noviembre 22)
# PRONTO EMPEZAMOS, GRACIAS POR LA ESPERA

import pandas as pd

 #Problemas típicos en un dataframe (asumiendo que el archivo se cargue de forma correcta):
    # 1. datos nulos o faltantes
    # 2. filas/datos duplicadas
    # 3. tipos de datos incorrectos


    # 4. índices incorrectos
    # 5. formatos de nombres de columnas o nombres incorrectos
    # 6. consumo de memoria (dataframe demasiado grande)

    # (a) se carga el dataframe desde el archivo plano
df_air_quality = pd.read_csv("Air_Quality_Dirty.csv")

# (b) visualizar información del dataframe:
df_air_quality.info()

#----- 1. datos nulos o faltanes en un dataframe:

#se identificó una columna donde todos los valores son nulos, descartar columna
# se usa la función drop : nombre de la columna, elimina en el mismo dataframe,
# axis corresponde al eje del dataframe: axis = 1, corresponde a las columnas (eje vertical)
#                                       axis = 0, corresponde a las filas (eje horizontal)
df_air_quality.drop("Message",inplace=True,axis=1)
df_air_quality.info()

# se eliminan después todas las filas en las que al menos una columna tenga un valor vacío
df_air_q_clean1 = df_air_quality.dropna()
df_air_q_clean1.info()

#---------- 2. Verificar Duplicados
#mostrar qué filas están duplicadas:
print(df_air_q_clean1.duplicated())

df_dup = df_air_q_clean1[df_air_q_clean1.duplicated()]
print(df_dup.info())
print(df_dup)

#eliminar filas duplicadas del dataframe:
df_air_q_clean1.drop_duplicates(inplace=True)

#----------- 3. Corregir formato de datos

