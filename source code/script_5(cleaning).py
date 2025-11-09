import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Paths for input and output 
# select your path correctly
# path = N:\Interview Q\p\clean.csv and "N:\Interview Q\p\after_clean.csv" this path is save your output file
input_path = r"N:\Interview Q\p\clean.csv"
output_path = r"N:\Interview Q\p\after_clean.csv"

# Load data
pn = pd.read_csv(input_path, parse_dates=["Order_Date", "Shipment_Date"], low_memory=False)

# Feature engineering
# ensure Total_Revenue exists
if "Total_Revenue" in pn.columns:
    pn["Total_Revenue"] = pn["Total_Revenue"]
else:
    pn["Total_Revenue"] = pn["Price"] * pn["Quantity"]

# time features
pn["Order_mouth"] = pd.to_datetime(pn["Order_Date"]).dt.month
pn["Order_Weekday"] = pd.to_datetime(pn["Order_Date"]).dt.weekday
pn["Order_year"] = pd.to_datetime(pn["Order_Date"]).dt.year
pn = pn.sort_values("Order_Date")

# rolling features (use a window appropriate for your frequency; example: 24 for 24 hours if hourly)
# Here using transaction-level rolling by index — for real production use time-based windows
pn["rolling_mean_10"] = pn["Total_Revenue"].rolling(window=10, min_periods=1).mean()
pn["rolling_std_10"]  = pn["Total_Revenue"].rolling(window=10, min_periods=1).std().fillna(0)
pn["pct_change"] = pn["Total_Revenue"].pct_change().fillna(0) * 100 #it show percentage format

# Z-score anomaly
pn["z_score"] = (pn["Total_Revenue"] - pn["rolling_mean_10"]) / (pn["rolling_std_10"].replace(0, np.nan))
pn["anomaly_z"] = (pn["z_score"].abs() > 3).astype(int)
pn["anomaly_z"] = pn["anomaly_z"].fillna(0).astype(int)

# Isolation Forest  
# Use numeric features that make sense: Total_Revenue, pct_change, quantity, maybe hour
features = ["Total_Revenue", "pct_change", "Quantity"] if "Quantity" in pn.columns else ["Total_Revenue", "pct_change"]
# Fill NaNs
X = pn[features].fillna(0).values

clf = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
clf.fit(X)
pn["anomaly_if"] = (clf.predict(X) == -1).astype(int)

# Combined flag
pn["anomaly"] = ((pn["anomaly_z"] == 1) | (pn["anomaly_if"] == 1)).astype(int)

# Save
pn.to_csv(output_path, index=False)
print("Saved processed with anomalies:", output_path)




