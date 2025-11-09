import pandas as pd

# STEP 1: Load the Excel file
# select your path correctly
# path = "N:\Interview Q\p\project.xlsx"

file_path = r"N:\Interview Q\p\project.xlsx"
pn = pd.read_excel(file_path)

# check
print("Preview of dataset what is inside the dateset")
print(pn.head())

# STEP 2: Check Missing Values

print("Missing calues check (Before Cleaning)")
print(pn.isnull().sum())

# it Show total missing cells in whole dataset
print("Total missing values:", pn.isnull().sum().sum())

# missing percentage as per column
missing_percent = (pn.isnull().sum() / len(pn)) * 100
print("Missing Percentage per Column")
print(missing_percent)

# STEP 3: Fix Missing Values

# Total_Revenue calculation
if "Price" in pn.columns and "Quantity" in pn.columns:
    pn["Total_Revenue"] = pn["Total_Revenue"].fillna(pn["Price"] * pn["Quantity"])

# Fill the missing 

if "Coupon_Code" in pn.columns:
    pn["Coupon_Code"] = pn["Coupon_Code"].fillna("No Coupon Code")

# Drop rows where critical_info is the missing
pn = pn.dropna(subset=["Order_Date", "Product_ID"])

# STEP 4: Verify After Cleaning
print("Missing Values Check (After Cleaning)")
print(pn.isnull().sum())

print("Data Shape After Cleaning")
print(pn.shape)

# STEP 5: Save Cleaned Data
output_path = r"N:\Interview Q\p\clean.csv"
pn.to_csv(output_path, index=False)
print(f"Cleaned dataset saved to: {output_path}")

# STEP 6: View 5 Rows

print("Check Final 5 Rows of Cleaned Data")
print("the data is clean or not")
print(pn.tail())





