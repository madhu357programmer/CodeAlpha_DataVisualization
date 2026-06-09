import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visuals folder
os.makedirs("visuals", exist_ok=True)

# Load dataset
df = pd.read_csv(
    "data/sales_data_sample.csv",
    encoding="latin1"
)

print("Dataset Loaded Successfully")
print(df.head())

# -----------------------------------
# Data Cleaning
# -----------------------------------

df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# -----------------------------------
# 1. Sales by Product Line
# -----------------------------------

sales_product = (
    df.groupby("PRODUCTLINE")["SALES"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))
sales_product.plot(kind="bar")
plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_productline.png")
plt.close()

# -----------------------------------
# 2. Monthly Sales Trend
# -----------------------------------

monthly_sales = (
    df.groupby("MONTH_ID")["SALES"]
    .sum()
)

plt.figure(figsize=(10,6))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/monthly_sales_trend.png")
plt.close()

# -----------------------------------
# 3. Sales by Country
# -----------------------------------

country_sales = (
    df.groupby("COUNTRY")["SALES"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
country_sales.plot(kind="bar")
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/top_countries_sales.png")
plt.close()

# -----------------------------------
# 4. Deal Size Distribution
# -----------------------------------

deal_size = (
    df.groupby("DEALSIZE")["SALES"]
    .sum()
)

plt.figure(figsize=(7,7))
deal_size.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Sales Distribution by Deal Size")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visuals/dealsize_distribution.png")
plt.close()

# -----------------------------------
# 5. Correlation Heatmap
# -----------------------------------

numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(10,8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
plt.close()

print("\nAll Visualizations Created Successfully!")