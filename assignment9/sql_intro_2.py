import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    query = """
    Select line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, products.price
    From line_items
    Join products ON line_items.product_id = products.product_id"""

    df = pd.read_sql_query(query, conn)

print("--- First 5 rows of the DataFrame ---")
print(df.head())

df['total'] = df['quantity'] * df['price']

print("\n--- First 5 rows with the 'total' column ---")
print(df.head())


summary_df = df.groupby('product_id').agg(
    total_ordered=('line_item_id', 'count'),
    product_name=('product_name', 'first'),
    total_revenue=('total', 'sum')
).reset_index()

print("\n--- Summary grouped by product_id ---")
print(summary_df.head())

summary_df = summary_df.sort_values(by='product_name')

summary_df.to_csv("order_summary.csv", index=False)
print("\nSummary successfully written to order_summary.csv")
