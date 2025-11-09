import pandas as pd

# select your path correctly
# path = "N:\Interview Q\p\project.xlsx"

file_path = r"N:\Interview Q\p\project.xlsx"
nt = pd.read_excel(file_path)  
print(nt.head())
print(nt.info())

print(nt.head(10))       
print(nt.columns) 
print(nt.info()) 
print(nt.describe(include='all').T)
