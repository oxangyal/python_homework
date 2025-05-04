import sqlite3

def get_total_price_of_first_five_orders():
    with sqlite3.connect("../db/lesson.db") as conn:
         print("Database created and connected successfully.")

    cursor = conn.cursor()

    # SQL query to get the total price of each of the first 5 orders
    query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """

    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(f"Order ID: {row[0]}, Total Price: {row[1]:.2f}")

    conn.close()

if __name__ == "__main__":
    get_total_price_of_first_five_orders()