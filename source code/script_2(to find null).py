import pandas as pd
# select your path correctly
# path = "N:\Interview Q\p\project.xlsx"

file_path = r"N:\Interview Q\p\after_clean.csv"
df = pd.read_csv(file_path) 
print(df.isnull().sum())
