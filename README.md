# 📦 Amazon_like E-Commerce Sales Monitoring 🔎 System. 🛒

---

# 🚀 Project Overview

This project is an **end-to-end data analytics pipeline that monitors** Amazon-style **e-commerce transactions in near real-time**.<br>
Python is used for **data cleaning, feature engineering, and outlier detection**. The processed data is then **stored in MySQL**, and Power BI connected in DirectQuery mode is used to **visualise real-time KPIs**.

---
# 🏗️ Architecture

<img width="2257" height="764" alt="Architecture" src="https://github.com/user-attachments/assets/20cab6cb-9d35-474d-9f6d-5719a56d2aa9" />

---
# 🧩 Tech Stack
| Layer                 | Tool                                     | Purpose                                    |
| --------------------- | ---------------------------------------- | ------------------------------------------ |
| 🧹 Data Cleaning      | Python (Pandas, NumPy)                   | Handle nulls, format dates, compute totals |
| 🧠 Model Logic        | Scikit-Learn (IsolationForest + Z-Score) | Detect unusual sales patterns              |
| 💾 Storage            | MySQL                                    | Central database for analytics             |
| ⚙️ Ingestion Pipeline | SQLAlchemy + Python                      | Push processed data to MySQL               |
| 📊 Visualization      | Power BI                                 | Live dashboard via DirectQuery             |
| ⚡ Realtime Simulation | Python (time module)                     | Stream random live transactions            |

---
# 🧮 Dataset

**Original source: [project.xlsx](https://github.com/user-attachments/files/23438663/project.xlsx)** <br><br>
**Columns include:** <br>
Order_ID, Order_Date, Shipment_Date, Customer_ID, Product_ID, Product_Name, Category, Price, Quantity, Discount, Total_Revenue, Payment_Method, Delivery_Status, Ratings etc. 
<br><br>
The  Rows represent real world style e-commerce orders (sales).

---

# ⚙️ How to Run and Requirements

### ⬇️ Install dependencies 

**One single pip command that installs everything** needed for DA Project (SQLAlchemy, Pandas, NumPy, etc.) all at once.

```
pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter notebook sqlalchemy pymysql

```
This pip code for **Upgrdes Dependencie**

```
py -m pip install --upgrade pip

```

### ⬇️ All file source Download

### 🛠️ Run And Setup

**Step 1: Create Database and Table**

- Set up a new database in MySQL.

- Create the required tables and define appropriate schema (columns, datatypes, and constraints).
<br>

**Step 2: Implement SQL Queries from Source Code**
<br>
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/ee2e7ec1-4d31-4e88-b1fb-0178ababf814" />

- Verify that the data Structure is inserted correctly into the table.
<br>

**Step 3: Data Validation (Run Script Lines 1–3)**  
Execute the first three lines of your Python script.

This section performs essential **data validation tasks**, including:

- Reading data from source files (`CSV`, `Excel`, or `JSON`)
- Checking for **missing (null)** values
- Detecting and **removing duplicate** records
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/75cae51b-4e2c-4d5a-81f3-df728dcdb8c5" />

<br>

**Step 4: Run the Script in VS Code / Terminal / Jupyter Lab**

- Open your development environment (VS Code, Terminal, or Jupyter Lab)[I ues vs-code].
- Execute your Python (or SQLAlchemy) script line by line — typically lines 4 to 6 contain the connection and data load logic.
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f41dbd79-fe79-4d18-9d00-51ec027e4164" />

- Wait for the script to execute successfully without errors.
<br>

**Step 5: Verify the Data in MySQL**

- Open MySQL Workbench or use a SELECT query to check whether the data has been successfully inserted.
```sql
SELECT * FROM orders;
```
- Ensure all rows and columns appear correctly before proceeding to Power BI integration.
  <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/fe165f4d-4481-498f-929d-ed094c9a706e" />

<br>

**Step 6: Connect MySQL Database to Power BI**

- Open Power BI Desktop and create a new report.

- Go to Get Data → MySQL Database.<br>
<img width="1920" height="1011" alt="Screenshot 2025-11-09 182516" src="https://github.com/user-attachments/assets/b4cb045c-b0ad-4f40-b8f5-ff13f6cbda9a" />
<br>

- Enter your server name, database name, username, and password.<br>
  
<img width="1920" height="1020" alt="Screenshot 2025-11-09 182803" src="https://github.com/user-attachments/assets/26a13d65-a6f4-472c-8ff3-c98dfcd57d40" />

- Load the table data into Power BI.
<br>

**Step 7: Build an Interactive Dashboard**

- Create charts, KPIs, slicers, and filters to visualize the data.

- Add interactivity and proper formatting for better analysis.

- Save and publish the dashboard to the Power BI Service for sharing or online access.

<br>

**Step 8: Real-Time Data Simulation**

- **The final script (Line 7) handles real-time data simulation.**

- It **automatically inserts new rows into the MySQL database every 20 seconds**, allowing live and continuous updates in Power BI.

- 🕒 The simulation runs indefinitely until you **close the terminal or exit the application**, at which point the data insertion **process stops automatically.**
- Ensure the password is set to **root: loop%40123**
 
<img width="1920" height="1017" alt="Screenshot 2025-11-09 185947" src="https://github.com/user-attachments/assets/b04a4a61-5acd-421f-818a-d7c5b0dda0b0" />

---

# 📊 DashBorad/ Report
### ☑️ All Mesures
```
Avg_Customer_Rating = AVERAGE('amazon_project orders'[ratings])
```
```
Total Profit = SUM('amazon_project orders'[Profit])         
```
```
total_orders = COUNT('amazon_project orders'[order_id])
```
```
Total_Quantity_sell = SUM('amazon_project orders'[quantity])
```
### 🔎 DashBorad Overview
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/420135df-df99-41b4-82f2-3b3992dae061" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/86ded284-66d7-4b78-9536-40fec8514001" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/a1032c79-3ded-4074-b3a5-6a8828c55b32" />

### ⚠️Erorr Shows(Only Using My DashBorad)

![WhatsApp Image 2025-11-09 at 12 39 25_ca1e7581](https://github.com/user-attachments/assets/413fd32f-ad80-4d25-b6e9-ce99325defed)

***👨‍🔧how to fix*** 
- Click Transform Data → Go Error → Choose DB
- Ensure you select the correct database.
---
# 💡 Note:
The main execution lies in Script Lines 4–6 — these handle the complete database connection and data loading process for the entire project.

If **Script Lines 1–3** (data validation steps) **fail or are skipped**, **it won’t affect the project execution**. The **focus should remain on running Lines 4–6**, as they form the **core operational logic** of this project.

# ⚙️ Follow all the steps sequentially within the script to ensure smooth and accurate execution of the entire process.










