import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Samiksha@30",
    database="ecommerce_analysis"
)

query = "SELECT * FROM sales"

df = pd.read_sql(query, connection)

print(df.head())
print("\nTotal records:", len(df))
print("\nTotal Revenue:", (df["quantity"] * df["price"]).sum())
print("\nDataset information:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nColumn names:")
print(df.columns.tolist())
df["revenue"] = df["quantity"] * df["price"]

print("\nRevenue added:")
print(df[["product_name", "quantity", "price", "revenue"]].head())
product_revenue = (
    df.groupby("product_name")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRevenue by Product:")
print(product_revenue)
category_revenue = (
    df.groupby("category")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRevenue by Category:")
print(category_revenue)
region_revenue = (
    df.groupby("region")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRevenue by Region:")
print(region_revenue)
df["order_date"] = pd.to_datetime(df["order_date"])

monthly_revenue = (
    df.groupby(df["order_date"].dt.month_name())["revenue"]
      .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)
import matplotlib.pyplot as plt

print("\nChecking region revenue:")
print(region_revenue)
plt.bar(region_revenue.index, region_revenue.values)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Monthly Revenue Chart

monthly_revenue = (
    df.groupby(df["order_date"].dt.month_name())["revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)

plt.figure(figsize=(8, 5))
plt.bar(monthly_revenue.index, monthly_revenue.values)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
highest_month = monthly_revenue.idxmax()
highest_revenue = monthly_revenue.max()

print("\nHighest Revenue Month:")
print(highest_month)
print(highest_revenue)
best_product = product_revenue.idxmax()
best_product_revenue = product_revenue.max()

print("\nBest Selling Product:")
print(best_product)
print(best_product_revenue)
best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

print("\nBest Category:")
print(best_category)
print(best_category_revenue)
best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

print("\nBest Category:")
print(best_category)
print(best_category_revenue)
customer_revenue = (
    df.groupby("customer_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Customers:")
print(customer_revenue.head(10))
top_customers = customer_revenue.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_customers.index, top_customers.values)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Revenue by Category Chart

plt.figure(figsize=(8, 5))
plt.bar(category_revenue.index, category_revenue.values)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

category_percentage = (
    category_revenue / category_revenue.sum() * 100
)

print("\nCategory Revenue Percentage:")
print(category_percentage.round(2))
print("\nCategory Contribution:")
print(category_percentage.round(2))
plt.figure(figsize=(7, 7))

plt.pie(
    category_percentage,
    labels=category_percentage.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Contribution by Category")
plt.show()
plt.show()
plt.figure(figsize=(7, 7))

plt.pie(
    category_percentage,
    labels=category_percentage.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Contribution by Category")
plt.show()
units_by_product = df.groupby("product_name")["quantity"].sum()

best_selling_product = units_by_product.idxmax()
highest_units = units_by_product.max()

print("\nBest Selling Product by Units:")
print(best_selling_product)
print(highest_units)
average_order_value = df["revenue"].mean()

print("\nAverage Order Value:")
print(round(average_order_value, 2))
total_units_sold = df["quantity"].sum()

print("\nTotal Units Sold:")
print(total_units_sold)
total_units_sold = df["quantity"].sum()

print("\nTotal Units Sold:")
print(total_units_sold)
average_price = (
    df.groupby("product_name")["price"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Price by Product:")
print(average_price.round(2))
region_percentage = (
    region_revenue / region_revenue.sum() * 100
)

print("\nRevenue Percentage by Region:")
print(region_percentage.round(2))
average_quantity = df["quantity"].mean()

print("\nAverage Quantity per Order:")
print(round(average_quantity, 2))
highest_order = df.loc[df["revenue"].idxmax()]

print("\nHighest Value Order:")
print(highest_order[["order_id", "customer_name", "product_name", "quantity", "price", "revenue"]])
# Top 10 Customers Chart

top_customers = customer_revenue.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_customers.index, top_customers.values)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
category_region_revenue = (
    df.groupby(["category", "region"])["revenue"]
    .sum()
)

print("\nRevenue by Category and Region:")
print(category_region_revenue)
print("\nCategory and Region Revenue:")
print(category_region_revenue)
# Highest Revenue Category in Each Region

highest_category_by_region = (
    df.groupby(["region", "category"])["revenue"]
      .sum()
      .groupby(level=0)
      .idxmax()
)

print("\nHighest Revenue Category in Each Region:")
print(highest_category_by_region)
# Lowest Revenue Month

lowest_month = monthly_revenue.idxmin()
lowest_revenue = monthly_revenue.min()

print("\nLowest Revenue Month:")
print(lowest_month)
print(lowest_revenue)
# Difference between Highest and Lowest Revenue Month

revenue_difference = highest_revenue - lowest_revenue

print("\nRevenue Difference:")
print(revenue_difference)
# Average Revenue per Unit

average_revenue_per_unit = df["revenue"].sum() / df["quantity"].sum()

print("\nAverage Revenue per Unit:")
print(round(average_revenue_per_unit, 2))

connection.close()