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

# ----------- Desarrollo actividad -------------------

# (a) Determinar cuales son los errores posibles / necesidades de analisis
#              ¿Cuales son las columnas importantes en la fase 3 del Worklow? R/: NCT Number,Title, Acronym, Status, Age
#              ¿Identificar cuales osn los posibles errores presentes en esas columnas
#              -> Formato de datos (numerico, real o entero, cadena de caracteres): astype
#              -> Rango de datos ( Validacion de acuerdo a los valores que se requieren)
#                     ej: Edad de personas no admiten numeros negativos, rango de años, meses
#              Iterar sobre el dataframe y analizar cada una de las columnas importantes

import pandas as pd

# Se carga el dataframe desde el archivo plano
df_Covid_Clin1 = pd.read_csv('Ejercicios/sampleDatasets/COVID clinical trials.csv')
df_Covid_Clin1.info()

#se eliminan despues todas las filas en las que al menos una columna tenga un valor vacio
df_Cvd_cl1 = df_Covid_Clin1.dropna()
df_Cvd_cl1.info()

# Se eliminan los valores nulos
df_Covid_Clin1.dropna(inplace=True)
df_Covid_Clin1.info()

#mSe identifican las filas están duplicadas:
print(df_Covid_Clin1.duplicated())

#validando el rango o encontrando datos atípicos
df_Cvd = df_Covid_Clin1.astype({"Enrollment":"int64"})

for i,item in df_Cvd.head(15).iterrows():
    if item["Enrollment"] < 900 or item["Enrollment"] > 2000:
        print(item)
        #corregir los inscritos:
        df_Cvd.loc[i,"Enrollment"] = 900