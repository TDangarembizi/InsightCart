import pandas as pd
import numpy as np
from faker import Faker
import os
import re

fake = Faker()

# Base path (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(DATA_PATH, exist_ok=True)

# 1. Customers

num_customers = 1000

customers = []

domains = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]

for i in range(1, num_customers + 1):
    name = fake.name()

    email_name = name.lower().replace(" ", ".")
    domain = np.random.choice(domains)

    customers.append({
        "customer_id": i,
        "name": name,
        "email": f"{email_name}@{domain}",
        "country": fake.country(),
        "signup_date": fake.date_between(start_date="-3y", end_date="today")
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(os.path.join(DATA_PATH, "customers.csv"), index=False)

#load product data
products = pd.read_csv(os.path.join(DATA_PATH, "products.csv"))

#standardise ID for consistency
products.rename(columns={"asin": "product_id"}, inplace=True)

# 2. Sales

num_sales = 10000

sales = pd.DataFrame({
    "order_id": range(1, num_sales + 1),
    "customer_id": np.random.choice(customers_df["customer_id"], num_sales),
    "product_id": np.random.choice(products["product_id"], num_sales),
    "quantity": np.random.randint(1, 6, num_sales),
    "order_date": [
        fake.date_between(start_date="-1y", end_date="today")
        for _ in range(num_sales)
    ]
})

# Join product price
sales = sales.merge(products[["product_id", "price"]], on="product_id", how="left")
sales.rename(columns={"price": "unit_price"}, inplace=True)

# Calculate total
sales["total_price"] = sales["quantity"] * sales["unit_price"]

sales.to_csv(os.path.join(DATA_PATH, "sales.csv"), index=False)

print(f"Faker dataset generated at: {DATA_PATH}")