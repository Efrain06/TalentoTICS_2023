#Tarea 1: Lista de diccionarios, filtrado

# 1. cree un pequeño dataset con datos de libros (titulo, autor, ISBN,
#    paginas, precio, categoria ("Ciencias","Literatura") ) como lista de diccionarios
# 2. realizar los siguientes filtros usando filter y list comprehension:
#    2.1 Libros con precio mayor a $45.000
#    2.2 Libros de categoría "Literatura" con paginas > 500
#    2.3 un filtro inventado por ud.

# Dataset "Libros"


lista_libros_1 = [
    {"ISBN": "9788491051329", "titulo": "Orgullo y Prejuicio", "autor": "Jorge Franco", "precio_u":"35000.0", "pag":"440", "categoria": "literatura"},
    {"ISBN": "9789585433328", "titulo": "Rosario Tijeras", "autor": "Jorge Franco", "precio_u":"43000.0", "pag":"157", "categoria": "literatura"},
    {"ISBN": "9580483620", "titulo": "Memoria de mis putas tristes", "autor": "Gabriel Garcia Marquez", "precio_u":"52000.0", "pag":"109", "categoria": "literatura"},
    {"ISBN": "9584261622", "titulo": "Origen", "autor": "Dan Brown", "precio_u":"75000.0", "pag":"637", "categoria": "suspenso y terror"},
    {"ISBN": "9789588618760", "titulo": "Cincuenta sombras de grey", "autor": "E.L James", "precio_u":"55000.0", "pag":"541", "categoria": "erotica"}
]


# Realizar los siguientes filtros usando filter y list comprehension:


print("-------------------------------------------------------")

#Filtro usando "list comprehension":
lista_lib_cat = [  lib1 for lib1 in lista_libros_1 if lib1["categoria"] == "literatura"]
print(f"Los siguientes libros son de la categoria literatura:{lista_lib_cat}")

print("-------------------------------------------------------")

lista_lib_precio = [  lib2 for lib2 in lista_libros_1 if lib2[ "pag" ] >= "500"]
print(f"Los siguientes libros son de 500 hojas en adelante:{lista_lib_precio}")

print("-------------------------------------------------------")

# Filtro usando filter ser:
def filter_set(lista_libros_1, search_string):
	def iterator_func(x):
		for v in x.values():
			if search_string in v:
				return True
		return False
	return filter(iterator_func, lista_libros_1)
filtered_records = filter_set(lista_libros_1, "Jorge Franco")
print(f"Los libros por el autor Jorge Franco son: {list(filtered_records)}")