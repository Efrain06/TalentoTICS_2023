import pandas as pd
import json

 #------------ LEER UN ARCHIVO JSON (JAVASCRIPT OBJECT NOTATION ) ------------
    # json_file = input("Cuál es la ruta del archivo JSON?")
    # df_temps_json = pd.read_json(json_file)
    # print(f"Dataframe cargado desde un archivo json:\n{df_temps_json}")


#df_rows_data = 'Ejercicios/rows.json'
#datos = pd.read_json(df_rows_data, orient='records')

data = json.load(open('Ejercicios/rows.json'))

df = pd.DataFrame(data['meta'])
print(df)