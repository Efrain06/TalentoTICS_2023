import pandas as pd

#ACTIVIDAD:
""""
1. DESCARGAR CSV DEL ENLACE: https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD
2. DUPLICAR ALGUNAS FILAS
3. ELIMINAR VALORES EN ALGUNAS COLUMNAS
4. CARGAR EL DATAFRAME
5. REALIZAR LA LIMPIEZA RESPECTIVA

"""


#1. datos nulos o faltantes en un dataframe:
# (a) se carga el dataframe desde el archivo plano
df_Meteo_land = pd.read_csv('Ejercicios/Meteorite_Landings.csv')

# (b) visualizar informacion del dataframe:
df_Meteo_land.info()

# Se identifico una columna donde todos los valores son nulos, descartar columna:

df_Meteo_land.drop("year", inplace=True,axis=1)
df_Meteo_land.info()

#se eliminan despues todas las filas en las que al menos una columna tenga un valor vacio
df_ML_cl1 = df_Meteo_land.dropna()
df_ML_cl1.info()

#------------------- 2. Verificar Duplicados
#mostrar qué filas están duplicadas:
print(df_ML_cl1.duplicated())

df_dup = df_ML_cl1[df_ML_cl1.duplicated()]
print(df_dup.info())
print(df_dup)

#eliminar filas duplicadas del dataframe:
df_ML_cl1.drop_duplicates(inplace=True)