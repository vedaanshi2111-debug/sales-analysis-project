import pandas as pd

df = pd.read_csv('sales_data (3).csv')
print(df)

print(df.shape)
print(df.columns)
print(df.dtypes)

df = df.dropna()
df = df.drop_duplicates()

total_revenue = df['Total_Sales'].sum()
print("Total Revenue:", total_revenue)

best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
print("Best Selling Product:", best_product)