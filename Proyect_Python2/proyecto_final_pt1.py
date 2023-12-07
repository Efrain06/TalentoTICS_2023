# WORKLOW DA:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 1. CARGA DE DATOS -> 

# Se carga el dataframe desde el archivo plano 
df_Datos1 = pd.read_csv('Proyect_data/Dataset/Internet_proveedor.csv')
df_Datos1.info()

df_Datos2 = pd.read_csv('Proyect_data\Dataset\ingresos_proveedor.csv')
#df_Datos2.info()


# Se eliminan los valores nulos Dataset 1:
df_Datos1.dropna(inplace=True)
df_Datos1.info()

# Se eliminan los valores nulos Dataset 2:
df_Datos2.dropna(inplace=True)
#df_Datos2.info()

#mostrar qué filas están duplicadas Dataset 1:
print(df_Datos1.duplicated())

#mostrar qué filas están duplicadas Dataset 2:
print(df_Datos1.duplicated())

#eliminar filas duplicadas del dataframe Dataset 1:
df_Datos1.drop_duplicates(inplace=True)

#eliminar filas duplicadas del dataframe Dataset 2:
df_Datos2.drop_duplicates(inplace=True)

#Se seleccionan las siguientes columnas del dataframe "Internet_proveedor": 
df_Dt1_Tb = df_Datos1 [["AÑO","PROVEEDOR","No. SUSCRIPTORES"]]
df_Dt1_Tb.info()

#Se seleccionan las siguientes columnas del dataframe "igresos_proveedor": 
df_Dt2_Tb = df_Datos2 [["AÑO","PROVEEDOR","INGRESOS"]]
#df_Dt2_Tb.info()

# 3. Factorizacion (para analisis de correlacion)
df_Dt1_Cr = df_Dt1_Tb.apply(lambda x: pd.factorize(x)[0])
print(df_Dt1_Cr.corr())
print("...................................")
# 3. Factorizacion (para analisis de correlacion)
df_Dt2_Cr = df_Dt2_Tb.apply(lambda x: pd.factorize(x)[0])
#print(df_Dt2_Cr.corr())

# Se grafican los datos por tabla de calor  
plt.figure(figsize=(10,10))
corr = df_Dt1_Cr.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5) #
plt.title("Correlacion proveedores internet" )
plt.show()

print("...................................")

#grafico de agrupacion:
sb.histplot(df_Dt1_Cr["PROVEEDOR"], bins=20, kde=True)
plt.title("Distribucion puntajes por proveedor")
plt.show()

print("...................................")

sb.boxplot(x="AÑO", y="No. SUSCRIPTORES", data=df_Dt1_Tb)
plt.title("Distribucion puntajes ")
plt.show()

print("...................................")

# No importa que tengan distinto # de filas
df_all_data = pd.merge(df_Datos1, df_Datos2, on="AÑO", how="inner", copy=False )
print(df_all_data.head())
print("...................................")
print(df_all_data.tail())