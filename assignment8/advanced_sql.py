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


def create_order_for_perez_and_sons():
    print("\n Creating order for Perez and Sons'...")
    try:
        with sqlite3.connect("../db/lesson.db") as conn:
            conn.execute("PRAGMA foreign_keys = 1")
            cursor = conn.cursor()

            # Get customer_id
            cursor.execute("""
                SELECT c.customer_id FROM customers c
                WHERE c.customer_name  = "Perez and Sons"
            """)
            customer_id = cursor.fetchone()[0]

            # Get employee_id for Miranda Harris
            cursor.execute("""
                SELECT e.employee_id FROM employees e
                WHERE first_name = 'Miranda'
                AND last_name = 'Harris'
            """)

            employee_id = cursor.fetchone()[0]


            # Get the 5 least expensive product_ids
            cursor.execute("""
                SELECT p.product_id FROM products p
                ORDER BY p.price  ASC
                LIMIT 5
            """)

            product_ids = [row[0] for row in cursor.fetchall()]

            # Start transaction
            cursor.execute("BEGIN")

            # Insert into orders table and get order_id
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, DATE('now'))
                RETURNING order_id
            """, (customer_id, employee_id))

            order_id = cursor.fetchone()[0]

            # Insert line_items: 10 of each product
            for pid in product_ids:
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, 10)
                """, (order_id, pid))

            # Commit transaction
            conn.commit()
            print("Order created successfully with line items.")

            #Print line items
            print("\n Order contents:")
            cursor.execute("""
                SELECT li.line_item_id, li.quantity, p.product_name
                FROM line_items li
                JOIN products p ON li.product_id = p.product_id
                WHERE li.order_id = ?
            """, (order_id,))

            for row in cursor.fetchall():
                print(f"Line item ID: {row[0]}, Quantity: {row[1]}, Product: {row[2]}")

    except Exception as e:
        conn.rollback()
        print("Transaction rolled back due to error:", e)

if __name__ == "__main__":
        get_total_price_of_first_five_orders()
        get_average_order_price_per_customer()
        create_order_for_perez_and_sons()
