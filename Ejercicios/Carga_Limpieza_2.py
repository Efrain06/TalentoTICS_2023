# PRACTICA WORKLOW ANALISIS DE DATOS
# QUE ES EL ANALISIS DE DATOS?
# PROCESO SISTEMATICO DE APLICAR TECNICAS DE CARGA, LIMPIEZA, ANALISIS ESTADISTICO DE DATOS
# EVALUAR Y APOYAR LA TOMA DE DECISIONES


# WORKLOW DA:
# 1. CARGA DE DATOS -> 2. LIMPIEZA DE DATOS -> 3. ANÁLISIS -> 4. VISUALIZACIÓN
#
# (a) Determinar cuales son los errores posibles / necesidades de analisis
#              ¿Cuales son las columnas importantes en la fase 3 del Worklow?
#              ¿Identificar cuales osn los posibles errores presentes en esas columnas
#              -> Formato de datos (numerico, real o entero, cadena de caracteres): astype
#              -> Rango de datos ( Validacion de acuerdo a los valores que se requieren)
#                     ej: Edad de personas no admiten numeros negativos, rango de años, meses
#              Iterar sobre el dataframe y analizar cada una de las columnas importantes
#
# (b) Determinar como se van a corregir
#              -> Eliminacion de filas con valores nulos: drop, dropna
#              -> Eliminacion de columnas nulas: drop
#              -> Eliminacion de duplicados: drop_duplicated
# HACER EL EJERCO CON police.csv (Columnas driver_age_raw)

import pandas as pd

df_Police = pd.read_csv('Ejercicios/sampleDatasets/police.csv')
df_Police.info()

def drop_columns(df:pd.DataFrame, columns_list):
    for col_name in columns_list:
        df.drop(col_name, inplace=True, axis=1)

# Limpieza del dataset:
cols = ["country_name", "search_type"]
drop_columns(df_Police, cols)
df_Police.dropna(inplace=True)
df_Police.info()