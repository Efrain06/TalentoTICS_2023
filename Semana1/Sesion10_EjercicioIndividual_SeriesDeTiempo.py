# Talento TICs 2023
# Pyton 2

# Relacionando dos datasets
# Concatenacion y merge de dataset
import pandas as pd
import matplotlib.pyplot as plt

sales_data_pts = {
    "point_id": [1,2,3,4,5,6,7,8],
    "nombres": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "sales": [ 100.1, 200.0, 209.0, 420.0, 400.0, 250.0, 120.0, 88.0,]
}

sales_data_prod = {
    "point_id": [1,2,3,4,5,6,7,8],
    "prod_id": [11,23,31,44,55,86,37,18],
    "nomb_prod": ["l", "f", "s", "d", "n", "b", "k", "j"],
    "vlr_unit": [ 10.0, 20.0, 29.0, 42.0, 4.0, 22.0, 12.0, 8.0,]
}

df_sales_pt = pd.DataFrame(sales_data_pts)
df_sales_prod = pd.DataFrame(sales_data_prod)

print(df_sales_pt)
print(df_sales_prod)

# El merge, mezcla dos dataset, dataframe a partir de una columna comun;
# No importa que tengan distinto # de filas
df_all_data = pd.merge(df_sales_pt, df_sales_prod, on = "point_id")

df_group = df_all_data.groupby("prod_id")["vlr_unit"].mean().plot(kind="bar")
plt.show()
print(df_all_data)

