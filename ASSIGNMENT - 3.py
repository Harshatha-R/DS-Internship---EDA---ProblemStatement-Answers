#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime

df = pd.read_excel("DS Internship - EDA - Data.xlsx")


# In[5]:


# Q1a: Total sales by year
df['Year'] = pd.DatetimeIndex(df['Store Open']).year
total_sales_by_year = df.groupby('Year')['Sales'].sum()
print("Q1a - Total Sales by Year:\n", total_sales_by_year, "\n")


# In[6]:


# Q1b: Number of stores opened in 1991
stores_1991 = df[df['Year'] == 1991]['Store'].nunique()
print("Q1b - Stores opened in 1991:", stores_1991, "\n")


# In[8]:


# Q1c: Number of remodelled stores
remodelled_count = df[df['Store Modification'].str.contains("remodel|relocation|format change", case=False, na=False)]['Store'].nunique()
print("Q1c - Remodelled stores:", remodelled_count, "\n")


# In[10]:


# Q1d: Correlation between sales & total sq ft
correlation = df['Sales'].corr(df['Total Sq Ft'])
print("Q1d - Pearson correlation (Sales vs Total sq ft):", correlation, "\n")


# In[11]:


# Q1e: Most profitable super division
most_profitable_div = df.groupby('Super Division')['Sales'].sum().idxmax()
print("Q1e - Most profitable super division:", most_profitable_div, "\n")


# In[15]:


# Q1f: Active stores
open_stores = df[~df['Store Close'].str.contains("Closed", case=False, na=False)]['Store'].nunique()
print("Q1f - Unique stores that have not closed:", open_stores)


# In[20]:


# Q1g: Super division with highest avg sq ft
highest_avg_sqft = df.groupby('Super Division')['Total Sq Ft'].mean().idxmax()
print("Q1g - Highest avg sq ft:", highest_avg_sqft, "\n")


# In[32]:


df_sorted = df.sort_values(by=['Store', 'Year'])
latest_status = df_sorted.groupby('Store').tail(1)
active_latest = latest_status[~latest_status['Store Close'].str.contains("Closed", case=False, na=False)]
top_states = active_latest['State'].value_counts().head(3).index.tolist()
print("Q2a - Top 3 candidate states:", top_states)


# In[30]:


df["Year"] = pd.to_datetime(df["Year"], errors="coerce")
df["Month-Year"] = df["Year"].dt.to_period('M')
best_time = df.groupby("Month-Year")["Sales"].sum().idxmax()
print("Q2b - Best time to open store:", best_time)


# In[ ]:


df['Store Close'] = df['Store Close'].astype(str)
closed_all = df[df['Store Close'].str.contains("Closed", case=False, na=False)]
closure_by_type_counts = closed_all['Outlet Type'].value_counts()
print("Closed store counts by outlet type:\n", closure_by_type_counts, "\n")
print("Outlet type with most closures:", closure_by_type_counts.idxmax())

