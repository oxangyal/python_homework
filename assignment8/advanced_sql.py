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


def get_average_order_price_per_customer():
    with sqlite3.connect("../db/lesson.db") as conn:
        print("\nCalculating average order price per customer...")

    cursor = conn.cursor()

    query = """
    SELECT
        c.customer_name,
        AVG(order_totals.total_price) AS average_total_price
    FROM
        customers c
    LEFT JOIN (
        SELECT
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price
        FROM
            orders o
        JOIN
            line_items li ON o.order_id = li.order_id
        JOIN
            products p ON li.product_id = p.product_id
        GROUP BY
            o.order_id, o.customer_id
    ) AS order_totals
    ON
        c.customer_id = order_totals.customer_id_b
    GROUP BY
        c.customer_id, c.customer_name;
    """

    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        name = row[0]
        avg_price = row[1]
        if avg_price is not None:
            print(f"{name}, Average Order Price: ${avg_price:.2f}")
        else:
            print(f"{name}, No orders.")


if __name__ == "__main__":
        get_total_price_of_first_five_orders()
        get_average_order_price_per_customer()
