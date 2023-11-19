#Talento TICS 2023 - Python2
#Noviembre 18, 2023
# Pandas, Matplotlib, NumPy

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import random as r

print(pd.__version__)

#cargar o crear informacion (datasets o dataframes)

#1. Crear dataframe de forma manual:

data = {
    "id": [1,2,3,4],
    "nombre": ["zapatillas converse", "Zapatillas Nike", "Zapatillas Adidas", "Zapatillas Diesel"],
    "precio_unit": [250000.0, 350000.0,380000.0,500000.0],
    "inv": [50, 25, 30 , 15]
}

#Convertir diccionario de datos en python a dataframe de pantas:
df_calzado = pd.DataFrame(data)
print(df_calzado)

#procesando un dataframe en pandas:
print(df_calzado.info())

#Seleccionando informacion de un dataframe:
print(df_calzado.head(2))
print(df_calzado.tail(1))

#seleccion de columnas:
print(df_calzado["nombre"])

#Seleccion de una fila en particular:
print(df_calzado.loc[2])

#Obtener estadistica descrptiva de columnas numericas:
print(df_calzado.describe())

#Obtener parametro estadistico de una columna en particular:
print(f"Promedio de inventario { df_calzado['inv'].mean()}")
print(f"Mediana de inventario { df_calzado['inv'].median()}")
print(f"Moda de inventario { df_calzado['inv'].mode()}")

#Agregar columna a un dataframe
df_calzado["descuento"] = [0.1,0.15,0.2,0.25]
df_calzado["bodega"] = ["centro", "centro", "sur", "norte"]
print(df_calzado)

#modificar datos fila 1, columna inventario:
df_calzado.at[1,"inv"] = 30

#Eliminar columna:
df_calzado = df_calzado.drop("bodega", axis=1)
print(df_calzado)

#Agregar una fila a un dataframe: PENDIENTE
nueva_fila = {"id": 1, "nombre": "Zapatillas Converse", "precio_u":250000.0, "inv":50}

#Eliminar fila:
df_calzado = df_calzado.drop(3)
print(df_calzado)

#Operaciones entre columnas:
#1. Agregar columna precio venta
df_calzado["precio_venta"] = [0.0, 0.0, 0.0]
print(df_calzado)

#Definir funcion de actualizacion:
def update_precio_venta(fila):
    return (fila["precio_unit"] - fila["precio_unit"] * fila["descuento"])

#Recorrer filas:
for fila in df_calzado.iterrows():
    print(fila)

#Aplicar funciones de actualizacion
df_calzado["precio_venta"] = df_calzado.apply(update_precio_venta, axis=1)
df_calzado["precio_venta"] = df_calzado.apply( lambda fila: fila["precio_unit"] - fila["precio_unit"] * fila["descuento"], axis=1 )
print(df_calzado)


#--------------------MATPLOLIB--------------------------

articulos = ["zapatillas converse", "Zapatillas Nike", "Zapatillas Adidas", "Zapatillas Diesel"]
ventas_tienda_centro = [150000, 180000, 200000, 300000]
ventas_tienda_sur = [186000, 200000, 250000, 380000]
ventas_tienda_norte = [120000, 150000, 290000, 330000]

#Crear un grafico de linea:
"""plot.plot(articulos,ventas_tienda_centro,label="ventas centro", marker='x')
plot.plot(articulos,ventas_tienda_sur,label="ventas sur", marker='x')
plot.plot(articulos,ventas_tienda_norte,label="ventas norte", marker='x')

plot.xlabel("Articulos")
plot.ylabel("ventas por tienda")
plot.title("ventas por articulo en tienda")

plot.legend()

plot.show()
"""
#---------------------PANDAS, MUMPY Y MATLOPLIB-------------------------

# Prestaciones de NumPy:
#1. Manejo de arreglos y matrices
#2. Aritmeticas, trigo, estad
#3. Indexacion y "slicing" (acceder a subconjuntos de datos multidimensionales)
#4. operaciones entre arreglos
#5. Eficiencia en manipulacion de listas

lista_meses = [1,2,3,4,5,6,7,8,9,10,11,12]
lista_dias = list(range(1,366,1))
lista_ventas_mes = []
lista_ventas_dias = []
lista_ventas_dias_2021 = []
lista_ventas_dias_2022 = []

for i in range(0,12,1):
    lista_ventas_mes.append(r.random())

for i in range(0,365,1):
    lista_ventas_dias.append(r.random())

print(lista_ventas_mes)
print(lista_ventas_dias)

#convertir de listas de python
array_ventas_mes = np.array(lista_ventas_mes)
array_ventas_dias_2021 = np.array(lista_ventas_dias_2021)
array_ventas_dias_2022 = np.array(lista_ventas_dias_2022)

array_ventas_dias_2021_2022 = array_ventas_dias_2021 + array_ventas_dias_2022
lista_ventas_dias_2021_2022 = lista_ventas_dias_2021 + lista_ventas_dias_2022 #¿?

# Prueba de que las listas en python no se operan aritmeticamente como en algebra lineal:
print( np.array([1,2,3,4] + np.array[5,6,7,8]))
print( np.array([1,2,3,4] - np.array[5,6,7,8]))
print( np.array([1,2,3,4] * np.array[5,6,7,8])) #producto vectorial ¿?
print( np.array([1,2,3,4] / np.array[5,6,7,8]))

#print(f"Ventas ultimos dos años:{array_ventas_dias_2021_2022}")
#print(f"Ventas ultimos dos años:{lista_ventas_dias_2021_2022}")



#Uso de pandas y Numpy:
datos_climaticos = {
    "meses":["enero", "febrero", "marzo", "abril", "mayo", "junio"],
    "temp_prom_2021":[28]
}