import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
# Note: The file might have encoding issues (we saw this in Postgres).
# Use 'latin1' to safely read it.
df = pd.read_csv('Sample-Superstore.csv', encoding='latin1')

# 2. First look: shape and data types
print("--- SHAPE ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- DATA TYPES & NULLS ---")
# This is the quickest way to spot missing values and wrong types
print(df.info())

# 3. Look at the actual data
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# 4. Basic stats for numerical columns
print("\n--- SUMMARY STATS ---")
print(df.describe())

# --- DATA CLEANING ---

# 1. Create a copy of the dataframe before changing anything
df_clean = df.copy()

# 2. Convert Order Date and Ship Date from text to datetime
# The format MM/DD/YYYY is common in the US, so we tell pandas exactly how to read it.
df_clean['Order Date'] = pd.to_datetime(
    df_clean['Order Date'], format='%m/%d/%Y')
df_clean['Ship Date'] = pd.to_datetime(
    df_clean['Ship Date'], format='%m/%d/%Y')

# 3. Check the new data types to confirm it worked
print("\n--- CLEANED DATA TYPES ---")
print(df_clean[['Order Date', 'Ship Date']].dtypes)

# 4. Feature Engineering: Calculate 'Days to Ship'
# Business logic: How long did the customer wait?
df_clean['Days to Ship'] = (
    df_clean['Ship Date'] - df_clean['Order Date']).dt.days

print("\n--- SHIPPING DAYS STATS ---")
print(df_clean['Days to Ship'].describe())

# --- VISUALIZATION ---
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

# Fixed the warning by adding hue and legend=False
sns.barplot(data=df_clean, x='Category', y='Profit', estimator=sum,
            errorbar=None, hue='Category', palette='viridis', legend=False)

plt.title('Total Profit by Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Profit ($)', fontsize=12)

plt.savefig('profit_by_category.png', dpi=300, bbox_inches='tight')
plt.show()


# --- SECOND VISUALIZATION: Discount vs Profit ---
plt.figure(figsize=(10, 6))

# Create a scatter plot
# alpha=0.5 makes the dots slightly transparent so you can see where they overlap
sns.scatterplot(data=df_clean, x='Discount',
                y='Profit', alpha=0.5, color='crimson')

# Add a horizontal line at 0 (the break-even point)
plt.axhline(y=0, color='black', linestyle='--')

plt.title('Impact of Discount on Profit', fontsize=16)
plt.xlabel('Discount Rate (0 = No discount, 1 = 100% off)', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)

# Save the chart
plt.savefig('discount_vs_profit.png', dpi=300, bbox_inches='tight')

# Show the chart
plt.show()

print("IF YOU SEE THIS, THE FILE IS SAVED AND RUNNING TO THE END.")
