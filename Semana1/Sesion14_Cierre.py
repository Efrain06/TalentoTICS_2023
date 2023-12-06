import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

df_prov = sb.load_dataset('Proyect_data/Dataset/Internet_proveedor.csv')
print(df_prov.sample(10))
print(df_prov.describe)

