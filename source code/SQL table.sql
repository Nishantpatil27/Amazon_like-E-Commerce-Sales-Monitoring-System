Create database amazon_project;
use amazon_project;

-- SELECT * FROM orders;

Create table orders (
    order_id varchar(50) primary key,
    order_date datetime not null,
    shipment_date datetime,
    customer_id varchar(50) not null,
    customer_name varchar(100),
    email varchar(100),
    city varchar(50),
    country VARCHAR(100),
    product_id varchar(50),
    product_name varchar(100),
    category varchar(50),
    product_link varchar(255),
    price decimal(20,2),
    quantity int,
    discount decimal(20,2),
    unit_sale int,
    coupon_code varchar(50),
    total_revenue decimal(20,2),
    payment_method varchar(50),
    delivery_status varchar(50),
    ratings decimal(3,2),
    order_month int,
    order_weekday varchar(15),
    order_year int,
    rolling_mean_10 decimal(20,2),
    rolling_std_10 decimal(20,2),
    pct_change decimal(20,2),
    z_score decimal(20,2),
    anomaly_z varchar(15),
    anomaly_if varchar(15),
    anomaly varchar(15)
); 

-- ALTER TABLE orders MODIFY COLUMN Country VARCHAR(100);

