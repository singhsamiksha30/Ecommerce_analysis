CREATE DATABASE ecommerce_analysis;
USE ecommerce_analysis;
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    region VARCHAR(50)
);
SHOW TABLES;
INSERT INTO sales
(order_id, order_date, customer_name, product_name, category, quantity, price, region)
VALUES
(1001, '2025-01-05', 'Rahul Sharma', 'Laptop', 'Electronics', 1, 55000, 'North'),
(1002, '2025-01-08', 'Priya Singh', 'Office Chair', 'Furniture', 2, 4500, 'South'),
(1003, '2025-01-12', 'Aman Verma', 'Headphones', 'Electronics', 3, 2000, 'West'),
(1004, '2025-01-15', 'Neha Gupta', 'Desk', 'Furniture', 1, 8000, 'East'),
(1005, '2025-01-20', 'Rohit Kumar', 'Keyboard', 'Electronics', 2, 1500, 'North');
SELECT *FROM sales;
SELECT 
    product_name,
    quantity,
    price,
    quantity * price AS revenue
FROM sales;
USE ecommerce_analysis;

INSERT INTO sales
(order_id, order_date, customer_name, product_name, category, quantity, price, region)

WITH RECURSIVE numbers AS (
    SELECT 1006 AS order_id
    UNION ALL
    SELECT order_id + 1
    FROM numbers
    WHERE order_id < 2005
)

SELECT
    order_id,

    DATE_ADD('2025-01-01', INTERVAL MOD(order_id * 17, 365) DAY) AS order_date,

    CASE MOD(order_id, 10)
        WHEN 0 THEN 'Aarav Sharma'
        WHEN 1 THEN 'Priya Singh'
        WHEN 2 THEN 'Rahul Verma'
        WHEN 3 THEN 'Neha Gupta'
        WHEN 4 THEN 'Aman Kumar'
        WHEN 5 THEN 'Riya Patel'
        WHEN 6 THEN 'Rohit Joshi'
        WHEN 7 THEN 'Ananya Mehta'
        WHEN 8 THEN 'Vikram Reddy'
        ELSE 'Sneha Das'
    END AS customer_name,

    CASE MOD(order_id, 10)
        WHEN 0 THEN 'Laptop'
        WHEN 1 THEN 'Smartphone'
        WHEN 2 THEN 'Headphones'
        WHEN 3 THEN 'Office Chair'
        WHEN 4 THEN 'Desk'
        WHEN 5 THEN 'Keyboard'
        WHEN 6 THEN 'Monitor'
        WHEN 7 THEN 'Backpack'
        WHEN 8 THEN 'Printer'
        ELSE 'Tablet'
    END AS product_name,

    CASE MOD(order_id, 10)
        WHEN 0 THEN 'Electronics'
        WHEN 1 THEN 'Electronics'
        WHEN 2 THEN 'Electronics'
        WHEN 3 THEN 'Furniture'
        WHEN 4 THEN 'Furniture'
        WHEN 5 THEN 'Electronics'
        WHEN 6 THEN 'Electronics'
        WHEN 7 THEN 'Accessories'
        WHEN 8 THEN 'Electronics'
        ELSE 'Electronics'
    END AS category,

    MOD(order_id, 5) + 1 AS quantity,

    CASE MOD(order_id, 10)
        WHEN 0 THEN 55000
        WHEN 1 THEN 30000
        WHEN 2 THEN 2000
        WHEN 3 THEN 4500
        WHEN 4 THEN 8000
        WHEN 5 THEN 1500
        WHEN 6 THEN 15000
        WHEN 7 THEN 1800
        WHEN 8 THEN 12000
        ELSE 22000
    END AS price,

    CASE MOD(order_id, 5)
        WHEN 0 THEN 'North'
        WHEN 1 THEN 'South'
        WHEN 2 THEN 'East'
        WHEN 3 THEN 'West'
        ELSE 'Central'
    END AS region

FROM numbers;
SELECT COUNT(*) AS total_records
FROM sales;
SELECT * 
FROM sales
LIMIT 20;
SELECT
    product_name,
    quantity,
    price,
    quantity * price AS revenue
FROM sales;
USE ecommerce_analysis;
SELECT 
    SUM(quantity * price) AS total_revenue
FROM sales;
SELECT 
    product_name,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;
SELECT
    category,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
SELECT
    region,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
SELECT
    MONTH(order_date) AS month_number,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY MONTH(order_date)
ORDER BY month_number;
SELECT
    MONTHNAME(order_date) AS month,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY MONTH(order_date), MONTHNAME(order_date)
ORDER BY MONTH(order_date);
SELECT
    customer_name,
    SUM(quantity * price) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC;
SELECT
    AVG(quantity * price) AS average_order_value
FROM sales;
SELECT
    product_name,
    SUM(quantity) AS units_sold,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;
SELECT
    region,
    COUNT(order_id) AS total_orders,
    SUM(quantity * price) AS total_revenue,
    AVG(quantity * price) AS average_order_value
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
SELECT
    product_name,
    SUM(quantity) AS units_sold,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY units_sold DESC;