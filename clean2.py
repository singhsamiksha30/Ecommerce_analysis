import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Samiksha@30",
    database="ecommerce_analysis"
)

# Load sales data
query = "SELECT * FROM sales"
df = pd.read_sql(query, connection)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

print("\nFirst 5 rows:")
print(df.head())
# Basic Data Analysis

total_revenue = df["revenue"].sum()
total_units = df["quantity"].sum()
average_order_value = df["revenue"].mean()

print("\n--- Business Summary ---")
print("Total Revenue:", total_revenue)
print("Total Units Sold:", total_units)
print("Average Order Value:", round(average_order_value, 2))

# Revenue by Product
product_revenue = (
    df.groupby("product_name")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Revenue by Product ---")
print(product_revenue)

# Revenue by Category
category_revenue = (
    df.groupby("category")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Revenue by Category ---")
print(category_revenue)

# Revenue by Region
region_revenue = (
    df.groupby("region")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Revenue by Region ---")
print(region_revenue)
# Monthly Revenue Analysis

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_revenue = (
    df.groupby(df["order_date"].dt.month_name())["revenue"]
      .sum()
)

print("\n--- Monthly Revenue ---")
print(monthly_revenue)

highest_month = monthly_revenue.idxmax()
highest_month_revenue = monthly_revenue.max()

lowest_month = monthly_revenue.idxmin()
lowest_month_revenue = monthly_revenue.min()

print("\nHighest Revenue Month:", highest_month)
print("Revenue:", highest_month_revenue)

print("\nLowest Revenue Month:", lowest_month)
print("Revenue:", lowest_month_revenue)
# Top Customers

customer_revenue = (
    df.groupby("customer_name")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Top 10 Customers ---")
print(customer_revenue.head(10))

top_customer = customer_revenue.idxmax()
top_customer_revenue = customer_revenue.max()

print("\nTop Customer:", top_customer)
print("Revenue:", top_customer_revenue)
# Product Performance

product_revenue = (
    df.groupby("product_name")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

units_by_product = (
    df.groupby("product_name")["quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Product Revenue ---")
print(product_revenue)

print("\n--- Units Sold by Product ---")
print(units_by_product)

best_revenue_product = product_revenue.idxmax()
best_units_product = units_by_product.idxmax()

print("\nHighest Revenue Product:", best_revenue_product)
print("Best-Selling Product by Units:", best_units_product)
# Visualizations

# 1. Revenue by Region
plt.figure(figsize=(8, 5))
plt.bar(region_revenue.index, region_revenue.values)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Revenue by Category
plt.figure(figsize=(8, 5))
plt.bar(category_revenue.index, category_revenue.values)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Monthly Revenue
plt.figure(figsize=(10, 5))
plt.bar(monthly_revenue.index, monthly_revenue.values)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Top 10 Customers

top_customers = customer_revenue.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_customers.index, top_customers.values)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Category Revenue Contribution

category_percentage = (
    category_revenue / category_revenue.sum() * 100
)

plt.figure(figsize=(7, 7))
plt.pie(
    category_percentage,
    labels=category_percentage.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Contribution by Category")
plt.show()
# Close MySQL connection
connection.close()

print("\nAnalysis completed successfully!")