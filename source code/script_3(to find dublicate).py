import pandas as pd
# select your path correctly
# path = "N:\Interview Q\p\project.xlsx" 

file_path = r"N:\Interview Q\p\project.xlsx"
df = pd.read_excel(file_path)  

df['Total_Amount'] = df['Total_Amount'].fillna(df['Price']*df['Quantity'])
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Shipment_Date'] = pd.to_datetime(df['Shipment_Date'])
print(df.head())
print(df.isnull().sum())