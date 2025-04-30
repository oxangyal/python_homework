import sqlite3
import pandas as pd

with sqlite3.connect("./db/lesson.db") as conn:

# SQL query to join line_items and products tables
    sql_statement = """
    SELECT line_items.line_item_id, line_items.quantity, line_items.product_id,
       products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """

# Read data into a DataFrame
    df = pd.read_sql_query(sql_statement, conn)
    print("Initial DataFrame:")
    print(df.head())

# Add a 'total' column
    df['total'] = df['quantity'] * df['price']
    print("\nDataFrame with 'total' column:")
    print(df.head())

# Group by product_id and aggregate
    summary_df = df.groupby('product_id').agg(
    line_item_count=('line_item_id', 'count'),
    total_sum=('total', 'sum'),
    product_name=('product_name', 'first')
    ).reset_index()
    print("\nGrouped by the product_id and aggregate:")
    print(df.head())


# Sort the DataFrame by product_name
    summary_df = summary_df.sort_values(by='product_name')
    print("\nSummary DataFrame:")
    print(summary_df.head())


# Write the summary DataFrame to a CSV file
    summary_df.to_csv("order_summary.csv", index=False)

conn.close()