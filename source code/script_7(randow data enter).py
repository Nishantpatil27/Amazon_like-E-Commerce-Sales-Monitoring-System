import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import time, random, uuid

# MySQL connection
# ensure you have choose your password and db name correctly
# my pass:-loop%401234 (loop = name, @ = %40, 1234= no.)

engine = create_engine("mysql+pymysql://root:loop%401234@localhost:3306/amazon_project")

# City–Country mapping
# for randiom city and contry selection
country_city_map = {
    'India': ['Mumbai', 'Delhi', 'Chennai', 'Bengaluru', 'Pune', 'Hyderabad'],
    'United States': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco'],
    'United Kingdom': ['London', 'Manchester', 'Birmingham'],
    'Canada': ['Toronto', 'Vancouver', 'Montreal'],
    'Germany': ['Berlin', 'Munich', 'Frankfurt'],
    'France': ['Paris', 'Lyon', 'Marseille'],
    'Japan': ['Tokyo', 'Osaka', 'Yokohama'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane'],
    'Brazil': ['São Paulo', 'Rio de Janeiro'],
    'Italy': ['Rome', 'Milan'],
    'United Arab Emirates': ['Dubai', 'Abu Dhabi'],
    'Singapore': ['Singapore'],
    'Malaysia': ['Kuala Lumpur', 'Penang'],
    'Mexico': ['Mexico City', 'Guadalajara'],
    'Spain': ['Madrid', 'Barcelona']
}

# --- Function to simulate one transaction ---
def generate_transaction():
    now = datetime.now()
    base_price = random.randint(50, 5000)
    qty = random.randint(10, 500)
    discount = random.choice([0, 5, 10, 15])
    unit_sale = base_price * qty
    total_rev = unit_sale - (unit_sale * discount / 100)
    
    country = random.choice(list(country_city_map.keys()))
    city = random.choice(country_city_map[country])

    return {
        'Order_ID': str(uuid.uuid4())[:8],
        'Order_Date': now,
        'Shipment_Date': now + timedelta(days=random.randint(1, 5)),
        'Customer_ID': f"C-{random.randint(11111, 99999)}",
        'Customer_Name': random.choice([
    'Amit', 'Rahul', 'Meena', 'Sara', 'Neha', 'Ravi', 'Ananya', 'Vikram', 'Priya', 'Arjun', 
    'Sneha', 'Karan', 'Rohit', 'Pooja', 'Dev', 'Manish', 'Aishwarya', 'Rajesh', 'Kavita', 'Nikhil',
    'Harshit', 'Rekha', 'Sanjay', 'Swati', 'Anjali', 'Isha', 'Abhishek', 'Deepak', 'Mohit', 'Kriti',
    'Tanvi', 'Aniket', 'Krishna', 'Ritika', 'Nisha', 'Siddharth', 'Gaurav', 'Harsha', 'Varun', 'Simran',
    'John', 'Emily', 'Michael', 'Sophia', 'Daniel', 'Emma', 'James', 'Olivia', 'Matthew', 'Isabella',
    'David', 'Charlotte', 'Andrew', 'Amelia', 'Joseph', 'Mia', 'Samuel', 'Grace', 'Benjamin', 'Chloe',
    'Nathan', 'Lily', 'Alexander', 'Ella', 'Jacob', 'Hannah', 'Luke', 'Scarlett', 'Henry', 'Ava',
    'Jack', 'Lucy', 'Noah', 'Ethan', 'Logan', 'Madison', 'Oliver', 'Zoe', 'William', 'Natalie',
    'Lucas', 'Marie', 'Julien', 'Camille', 'Antoine', 'Chloe', 'Hugo', 'Lea', 'Pierre', 'Emma',
    'Nicolas', 'Sarah', 'Thomas', 'Clara', 'Louis', 'Elodie', 'Paul', 'Ines', 'Alexandre', 'Manon',
    'Lukas', 'Anna', 'Leon', 'Mia', 'Jonas', 'Leonie', 'Finn', 'Lara', 'Felix', 'Sophie',
    'Noah', 'Emilia', 'Maximilian', 'Hannah', 'Moritz', 'Johanna', 'Sebastian', 'Mila', 'Tobias', 'Laura',
    'Yuki', 'Haruto', 'Sakura', 'Rina', 'Ren', 'Yui', 'Kaito', 'Hina', 'Takumi', 'Aya',
    'Daichi', 'Nana', 'Sota', 'Miku', 'Sho', 'Akira', 'Aoi', 'Kenta', 'Riko', 'Kei',
    'Carlos', 'Sofia', 'Mateus', 'Camila', 'Rafael', 'Isabela', 'Joao', 'Fernanda', 'Lucas', 'Gabriela',
    'Pedro', 'Larissa', 'Thiago', 'Beatriz', 'Bruno', 'Luana', 'Felipe', 'Mariana', 'Daniela', 'Andre',
    'Li Wei', 'Chen Yu', 'Wang Fang', 'Kim Min', 'Lee Hyun', 'Park Ji', 'Tan Wei', 'Nguyen Anh', 'Hoang Minh', 'Lim Siew',
    'Chen Lin', 'Wong Mei', 'Tan Jia', 'Yeo Ling', 'Chong Wei', 'Siti Nur', 'Aung Kyaw', 'Pham Huong', 'Tran Nam', 'Nurul Aini',
    'Marco', 'Giulia', 'Luca', 'Francesca', 'Alessandro', 'Chiara', 'Antonio', 'Martina', 'Diego', 'Elena',
    'Javier', 'Lucia', 'Miguel', 'Carmen', 'Pablo', 'Ines', 'Sergio', 'Rosa', 'Eduardo', 'Patricia'
]),
        'Email': f"user{random.randint(1000, 9999)}@gmail.com",
        'City': city,
        'Country': country,
        'Product_ID': f"PROD-{random.randint(100, 999)}",
        'Product_Name': random.choice(['Phone', 'Laptop', 'Headphones', 'Camera', 'Shoes', 'Watch', 'Bag']),
        'Category': random.choice(['Electronics', 'Fashion', 'Sports', 'Home']),
        'Product_Link': f"https://amazon.in/product/{random.randint(1000, 9999)}",
        'Price': base_price,
        'Quantity': qty,
        'Discount': discount,
        'unit_sale': unit_sale,
        'Coupon_Code': random.choice(['No Coupon Code', 'No Coupon Code','No Coupon Code','gzNOL-ZtoXa', 'gzNOL-ZooXa','uhwOL-ZooXa']),
        'total_revenue': total_rev,
        'Payment_Method': random.choice(['Credit Card', 'UPI', 'COD', 'NetBanking','PayPal']),
        'Delivery_Status': random.choice(['Delivered', 'Returned', 'Pending', 'Cancelled']),
        'Ratings': random.randint(1, 5),
        'Order_month': now.month,
        'Order_Weekday': now.weekday(),
        'Order_year': now.year,
        'rolling_mean_10': 0,
        'rolling_std_10': 0,
        'pct_change': 0,
        'z_score': 0,
        'anomaly_z': 0,
        'anomaly_if': 0,
        'anomaly': 0
    }

# --- Continuous simulation ---
batch_number = 1

while True:
    new_batch = [generate_transaction() for _ in range(5)]
    df = pd.DataFrame(new_batch)
    print(f"\n===  Batch {batch_number} Data ===")
    print(df[['Order_ID', 'Customer_Name', 'City', 'Country', 'Product_Name', 'Quantity', 'total_revenue']])
    print("=" * 70)

    # Insert into MySQL
    df.to_sql('orders', con=engine, if_exists='append', index=False)
    print(f"Batch {batch_number}: Inserted {len(df)} new rows at {datetime.now()}")

    verify_count = pd.read_sql("SELECT COUNT(*) as total FROM orders", con=engine)
    print(f"📊 Total rows now in 'orders' table: {verify_count['total'][0]}")

    # Verify insertion — fetch last 5 rows from 'orders' table
    verify_df = pd.read_sql(
        "SELECT Order_ID, Customer_Name, City, Country, Product_Name, Quantity, total_revenue "
        "FROM orders ORDER BY Order_Date DESC LIMIT 5", con=engine
    )
    print("\n Verified Latest 5 Rows in Database:")
    print(verify_df)
    print("=" * 70)

    batch_number += 1
    time.sleep(20)  # wait 20 seconds between inserts
