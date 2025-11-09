import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
# ensure you have choose your password and db name correctly
# my pass:-loop%401234 (loop = name, @ = %40, 1234= no.)
engine = create_engine("mysql+pymysql://root:loop%401234@localhost:3306/amazon_project")

# Load CSV
# select your path correctly
# path = "N:\Interview Q\p\after_clean.csv"
pn = pd.read_csv(r"N:\Interview Q\p\after_clean.csv")

# Convert date columns into datetime
date_cols = ['Order_Date', 'Shipment_Date']
for col in date_cols:
    pn[col] = pd.to_datetime(pn[col].replace('No Return', pd.NaT), errors='coerce')

# to match your MySQL table
pn = pn.rename(columns={
    'Order_ID': 'Order_ID',
    'Order_Date': 'Order_Date',
    'Shipment_Date': 'Shipment_Date',
    'Customer_ID': 'Customer_ID',
    'Customer_Name': 'Customer_Name',
    'Email': 'Email',
    'City': 'City', 
    'Country': 'Country',
    'Product_ID': 'Product_ID',
    'Product_Name': 'Product_Name',
    'Category': 'Category',
    'Product_Link': 'Product_Link',
    'Price': 'Price',
    'Quantity': 'Quantity',
    'Discount': 'Discount',
    'Unit Sale':'unit_sale',
    'Coupon_Code': 'Coupon_Code',
    'Total_Revenue': 'total_revenue',
    'Payment_Method': 'Payment_Method',
    'Delivery_Status': 'Delivery_Status',
    'Ratings': 'Ratings',
    'Order_mouth': 'Order_month',
    'Order_Weekday': 'Order_Weekday',
    'Order_year': 'Order_year',
    'rolling_mean_10': 'rolling_mean_10',
    'rolling_std_10': 'rolling_std_10',
    'pct_change': 'pct_change',
    'z_score': 'z_score',
    'anomaly_z': 'anomaly_z',
    'anomaly_if': 'anomaly_if',
    'anomaly': 'anomaly'
})

# convert numeric columns into int/float/decimal etc.
numeric_cols = ['Price', 'Quantity', 'Discount', 'total_revenue', 
                'Ratings', 'rolling_mean_10', 'rolling_std_10', 
                'pct_change', 'z_score']
for col in numeric_cols:
    pn[col] = pd.to_numeric(pn[col], errors='coerce')

# Insert into MySQL/other db
pn.to_sql('orders', engine, if_exists='append', index=False)

# If your code rum then print last line

print(f"{len(pn)} rows inserted into amazon_project.orders")


