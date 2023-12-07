# WORKLOW DA:


import pandas as pd
import matplotlib.pyplot as plt


# 1. CARGA DE DATOS -> 

# Se carga el dataframe desde el archivo plano "Perfil de morbilidad Julio"
df_dat_PM1 = pd.read_csv('Proyect_data\Dataset\Perfil_de_morbilidad_Julio.csv')
df_dat_PM1.info()

# Se carga el dataframe desde el archivo plano "Perfil de morbilidad Agosto"
df_dat_PM2 = pd.read_csv('Proyect_data\Dataset\Perfil_de_morbilidad_Agosto.csv')
df_dat_PM2.info()

# Se eliminan los valores nulos Dataset 1 y 2:
df_dat_PM1.dropna(inplace=True)
df_dat_PM2.dropna(inplace=True)

#eliminar filas duplicadas del dataframe Dataset 1 y 2:
df_dat_PM1.drop_duplicates(inplace=True)
df_dat_PM2.drop_duplicates(inplace=True)

# Serie de tiempo 
df_all_data = pd.merge(df_dat_PM1, df_dat_PM2, on="AÑO REPORTADO", how="inner", copy=False )
print(df_all_data.head())
print(".....................................................................")
print(df_all_data.info())
print(".....................................................................")
print(df_all_data.tail())
print(".....................................................................")

#adecuación del dataset para manejo de datos temporales:
df_Dat_Tmp = df_dat_PM2.rename(columns={"EDAD DE ATENCION (AÑOS)":"EDAD DE ATENCION"})
#valores inválidos con opción errors = "coerce", asigna NaN:
df_Dat_Tmp["EDAD DE ATENCION"] = pd.to_numeric(df_Dat_Tmp["EDAD DE ATENCION"],errors="coerce") 

print(f"dataset limpio:{df_Dat_Tmp.info()}")
print(".....................................................................")
print(df_dat_PM2.head(50))
print(".....................................................................")
print(f"La edad maxima de atencion es: ", df_Dat_Tmp["EDAD DE ATENCION"].max())
print(".....................................................................")
print(f"La edad minima de atencion es: ", df_Dat_Tmp["EDAD DE ATENCION"].min())
