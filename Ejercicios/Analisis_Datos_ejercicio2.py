<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Cargar el dataframe:
df_Sab11 = pd.read_csv('Ejercicios/sampleDatasets/Saber_11__2019-2.csv')
#df_Sab11.info()

# Limpieza del dataframe:
df_Sab11.dropna(inplace=True)
#df_Sab11.info()

# Se identifican las filas están duplicadas:
#print(df_Sab11.duplicated())
df_Sab11.drop_duplicates(inplace=True)

# Se seleccionan las columnas para analizar
df_Icfes = df_Sab11[["ESTU_GENERO", "ESTU_DEDICACIONLECTURADIARIA", "PUNT_LECTURA_CRITICA", "ESTU_ETNIA", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "FAMI_EDUCACIONPADRE", "FAMI_EDUCACIONMADRE", "PUNT_GLOBAL", "PERCENTIL_GLOBAL"]]
df_Icfes.info()

# Se realiza la factorizacion:
df_Icf = df_Icfes.apply(lambda x: pd.factorize(x)[0])
print(df_Icf.corr())

# Se grafican los datos por tabla de calor  
plt.figure(figsize=(10,10))
corr = df_Icf.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5) #
plt.title("Correlacion Pruebas Saber 11" )
plt.show()

#grafico de agrupacion:

#sb.histplot(df_Icf["FAMI_ESTRATOVIVIENDA"], bins=20, kde=True)
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()

#sb.violinplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf, inner="quartile")
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()

#sb.boxenplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf)
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()


sb.boxplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf)
plt.title("Distribucion puntajespor estrato socioeconomico")
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Cargar el dataframe:
df_Sab11 = pd.read_csv('Ejercicios/sampleDatasets/Saber_11__2019-2.csv')
#df_Sab11.info()

# Limpieza del dataframe:
df_Sab11.dropna(inplace=True)
#df_Sab11.info()

# Se identifican las filas están duplicadas:
#print(df_Sab11.duplicated())
df_Sab11.drop_duplicates(inplace=True)

# Se seleccionan las columnas para analizar
df_Icfes = df_Sab11[["ESTU_GENERO", "ESTU_DEDICACIONLECTURADIARIA", "PUNT_LECTURA_CRITICA", "ESTU_ETNIA", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "FAMI_EDUCACIONPADRE", "FAMI_EDUCACIONMADRE", "PUNT_GLOBAL", "PERCENTIL_GLOBAL"]]
df_Icfes.info()

# Se realiza la factorizacion:
df_Icf = df_Icfes.apply(lambda x: pd.factorize(x)[0])
print(df_Icf.corr())

# Se grafican los datos por tabla de calor  
plt.figure(figsize=(10,10))
corr = df_Icf.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5) #
plt.title("Correlacion Pruebas Saber 11" )
plt.show()

#grafico de agrupacion:

#sb.histplot(df_Icf["FAMI_ESTRATOVIVIENDA"], bins=20, kde=True)
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()

#sb.violinplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf, inner="quartile")
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()

#sb.boxenplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf)
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()


sb.boxplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf)
plt.title("Distribucion puntajespor estrato socioeconomico")
>>>>>>> 1cdc274401ee19ee41818e10c083de94bca4990c
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Cargar el dataframe:
df_Sab11 = pd.read_csv('Ejercicios/sampleDatasets/Saber_11__2019-2.csv')
#df_Sab11.info()

# Limpieza del dataframe:
df_Sab11.dropna(inplace=True)
#df_Sab11.info()

# Se identifican las filas están duplicadas:
#print(df_Sab11.duplicated())
df_Sab11.drop_duplicates(inplace=True)

# Se seleccionan las columnas para analizar
df_Icfes = df_Sab11[["ESTU_GENERO", "ESTU_DEDICACIONLECTURADIARIA", "PUNT_LECTURA_CRITICA", "ESTU_ETNIA", "ESTU_DEPTO_RESIDE", "FAMI_ESTRATOVIVIENDA", "FAMI_EDUCACIONPADRE", "FAMI_EDUCACIONMADRE", "PUNT_GLOBAL", "PERCENTIL_GLOBAL"]]
df_Icfes.info()

# Se realiza la factorizacion:
df_Icf = df_Icfes.apply(lambda x: pd.factorize(x)[0])
print(df_Icf.corr())

# Se grafican los datos por tabla de calor  
plt.figure(figsize=(10,10))
corr = df_Icf.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5) #
plt.title("Correlacion Pruebas Saber 11" )
plt.show()

#grafico de agrupacion:

#sb.histplot(df_Icf["FAMI_ESTRATOVIVIENDA"], bins=20, kde=True)
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()

#sb.violinplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf, inner="quartile")
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()

#sb.boxenplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf)
#plt.title("Distribucion puntajespor estrato socioeconomico")
#plt.show()


sb.boxplot(x="FAMI_ESTRATOVIVIENDA", y="PUNT_GLOBAL", data=df_Icf)
plt.title("Distribucion puntajespor estrato socioeconomico")
>>>>>>> 1cdc274401ee19ee41818e10c083de94bca4990c
plt.show()