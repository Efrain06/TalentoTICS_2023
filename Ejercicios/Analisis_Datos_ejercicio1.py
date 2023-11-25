import pandas as pd

# Se carga el dataframe: 
df_Mort_Tb = pd.read_csv('Ejercicios/sampleDatasets/Mortalidad_tuberculosis.csv')
df_Mort_Tb.info()

# Se seleccionan las siguientes columnas: 
df_MTb = df_Mort_Tb[ ["SEXO", "EST_CIVIL", "EDAD", "NIVEL_EDU", "OCUPACION", "SEG_SOCIAL", "CODMUNRE", "MUERTEPORO"]]
df_MTb.info()

# Eliminar los elementos nulos
df_MTb.dropna(inplace=True)
df_MTb.info()

# Imprimir valores unicos de una columna:
print(f"Valores unicos de estado civil: {df_MTb['EST_CIVIL'].unique()}")
# Se identifican algunos valores que difieren en un espacio:

for i,row in df_MTb.iterrows():
    df_MTb.loc[1,"EST_CIVIL"] = str(row["EST_CIVIL"]).strip()    # Strip elimina espacios al inicio o al final
    df_MTb.loc[1,"NIVEL_EDU"] = str(row["NIVEL_EDU"]).strip()

print(f"Valores est civil:{df_MTb['EST_CIVIL'].unique().__len__()}")
print(df_MTb["EST_CIVIL"].unique())
print(df_MTb["NIVEL_EDU"].unique())
print(df_MTb["SEXO"].unique())

# Filtrado de filas
df_MTb_f = df_MTb[ df_MTb["SEXO"] == "Femenino"]
df_MTb_f = df_MTb[ df_MTb["SEXO"] == "Masculino"]

# 3. Factorizacion (para analisis de correlacion)
df_MTb_i = df_MTb.apply(lambda x: pd.factorize(x)[0])
print(df_MTb_i.corr())