# WORKLOW DA:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 1. CARGA DE DATOS -> 

# Se carga el dataframe desde el archivo plano 
df_Datos1 = pd.read_csv('Proyect_Python2\Dataset\Internet_proveedor.csv')
df_Datos1.info()

# Se eliminan los valores nulos Dataset 1:
df_Datos1.dropna(inplace=True)
df_Datos1.info()

#mostrar qué filas están duplicadas Dataset 1:
print(df_Datos1.duplicated())


#eliminar filas duplicadas del dataframe Dataset 1:
df_Datos1.drop_duplicates(inplace=True)


#Se seleccionan las siguientes columnas del dataframe "Internet_proveedor": 
df_Dt1_Tb = df_Datos1 [["AÑO","PROVEEDOR","TECNOLOGÍA","No. SUSCRIPTORES"]]
df_Dt1_Tb.info()

# 3. Factorizacion (para analisis de correlacion)
df_Dt1_Cr = df_Dt1_Tb.apply(lambda x: pd.factorize(x)[0])
print(df_Dt1_Cr.corr())
print("...................................")


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

sb.violinplot(x="TECNOLOGÍA", y="No. SUSCRIPTORES", data=df_Dt1_Tb, inner="quartile")
plt.title("Distribucion puntajespor estrato socioeconomico")
plt.show()