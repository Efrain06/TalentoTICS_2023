import pandas as pd

    #---------------  LEER UN CSV ----------------
    #cargar información de un archivo plano csv con una función propia:
    #df_temps_manual = pd.DataFrame(cargaArchivoPlano_Python(file_name))
    #print(f"data set cargado manualmente:\n{df_temps_manual}")

    #cargar información de un archivo plano csv con pandas:
    # TENER EN CUENTA EL SEPARADOR DE LOS VALORES EN EL ARCHIVO
    # df_temps_pandas = pd.read_csv(file_name,sep=";")
    # print(f"Dataset cargado desde un csv con pandas:\n{df_temps_pandas}")

    #global education data
    #https://www.kaggle.com/datasets
    #https://www.kaggle.com/datasets/nelgiriyewithana/world-educational-data/
df_global_edu_data = pd.read_csv('Ejercicios\Global_Education.csv',sep=",")
df_global_edu_data.info()

print(df_global_edu_data.head(10))
