# Task 2: A Line Plot with Pandasimport sqlite3
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect("../db/lesson.db") as conn:

 # SQL to get order_id and total_price (price * quantity)
    query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    """

# Load the query results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()


# Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs. order_id
df.plot(
    x='order_id',
    y='cumulative',
    kind='line',
    title='Cumulative Revenue by Order ID',
    marker='o',
    color='skyblue'
)

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()