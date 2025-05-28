# Task 1: Plotting with Pandas
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect("../db/lesson.db") as conn:

# SQL query to get employee revenue
    query = """
    SELECT last_name, SUM(price * quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
    """

# Load the query results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Plotting
df.plot(
    x="last_name",
    y="revenue",
    kind="bar",
    color="skyblue",
    title="Employee Results"
)

plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()