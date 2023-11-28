import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Cargar el dataframe:
df_CD_medic = pd.read_csv('Ejercicios/sampleDatasets/CODIGO_MEDICAMENTOS_VIGENTES.csv')
#df_Sab11.info()

# Limpieza del dataframe:
df_CD_medic.dropna(inplace=True)
#df_Sab11.info()

# Se identifican las filas están duplicadas:
#print(df_Sab11.duplicated())
df_CD_medic.drop_duplicates(inplace=True)

# Se seleccionan las columnas para analizar
df_CD_Medic1 = df_CD_medic[["expediente", "producto", "registrosanitario", "fechavencimiento", "formafarmaceutica", "viaadministracion"]]
df_CD_Medic1.info()

# Se realiza la factorizacion:
df_CDM = df_CD_Medic1.apply(lambda x: pd.factorize(x)[0])
print(df_CDM.corr())

# Se grafican los datos por tabla de calor  
plt.figure(figsize=(10,10))
corr = df_CDM.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5) #
plt.title("Correlacion Medicamentos Vigentes" )
plt.show()

#grafico de agrupacion:

sb.histplot(df_CDM["producto"], bins=20, kde=True)
plt.title("Los medicamentos que se encuentran vigentes")
plt.show()

#sb.violinplot(x="formafarmaceutica", y="viaadministracion", data=df_CDM, inner="quartile")
#plt.title("Comparacion ")
#plt.show()

#sb.boxenplot(x="producto", y="registrosanitario", data=df_CDM)
#plt.title("Registro sanitario de cada producto")
#plt.show()


#sb.boxplot(x="producto", y="fechavencimiento", data=df_CDM)
#plt.title("Fecha de vencimiento por cada producto")
#plt.show()