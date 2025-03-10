import pandas as pd
import numpy as np

file_path = r"C:\Users\Borges\Documents\LukaDoncicStatsNBA.xlsx"

df = pd.read_excel(file_path, usecols="E", skiprows=0, nrows=8)

media = np.mean(df.iloc[:, 0])
mediana = np.median(df.iloc[:, 0])

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
