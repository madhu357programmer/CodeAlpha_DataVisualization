import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Dashboard")

# Load dataset
df = pd.read_csv(
    "data/sales_data_sample.csv",
    encoding="latin1"
)

df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# ----------------------------
# KPI Section
# ----------------------------

total_sales = df["SALES"].sum()
total_orders = df["ORDERNUMBER"].nunique()
countries = df["COUNTRY"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Countries", countries)

st.divider()

# ----------------------------
# Product Line Sales
# ----------------------------

st.subheader("Sales by Product Line")

product_sales = (
    df.groupby("PRODUCTLINE")["SALES"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
product_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Sales")

st.pyplot(fig)

# ----------------------------
# Monthly Trend
# ----------------------------

st.subheader("Monthly Sales Trend")

monthly_sales = (
    df.groupby("MONTH_ID")["SALES"]
    .sum()
)

fig, ax = plt.subplots(figsize=(8,4))
monthly_sales.plot(marker="o", ax=ax)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")

st.pyplot(fig)

# ----------------------------
# Top Countries
# ----------------------------

st.subheader("Top 10 Countries")

country_sales = (
    df.groupby("COUNTRY")["SALES"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(8,4))
country_sales.plot(kind="bar", ax=ax)

st.pyplot(fig)

# ----------------------------
# Raw Data
# ----------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head(20))