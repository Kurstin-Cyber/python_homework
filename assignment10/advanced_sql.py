import sqlite3

db_path = "../db/lesson.db"

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()


# Task 1: Complex JOINs with Aggregation

query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """
cursor.execute(query)
results = cursor.fetchall()

print("Task 1 Results (First 5 Orders & Totals):")
for row in results:
    order_id, total_price = row
    print(f"Order ID: {order_id} | Total Price: ${total_price:.2f}")

# Task 2: Understanding Subqueries


query_task2 = """
SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS sub ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id, c.customer_name;
"""
cursor.execute(query_task2)
results_task2 = cursor.fetchall()

print("\nTask 2 Results (Customer Average Order Totals):")
for row in results_task2:
    customer_name, avg_price = row
    display_avg = f"${avg_price:.2f}" if avg_price is not None else "No Orders"
    print(f"Customer: {customer_name} | Average Order Total: {display_avg}")


# Task 3: An Insert Transaction Based on Data

try:

    cursor = conn.cursor()

    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
    customer_row = cursor.fetchone()
    customer_id = customer_row[0] if customer_row else None

    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_row = cursor.fetchone()
    employee_id = employee_row[0] if employee_row else None
    
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    product_rows = cursor.fetchall()
    product_ids = [row[0] for row in product_rows]

    if customer_id is None or employee_id is None or len(product_ids) < 5:
        raise ValueError("Could not find required customer, employee, or 5 products.")
    
    cursor.execute("INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id;", (customer_id, employee_id))
    new_order_id = cursor.fetchone()[0]

    for prod_id in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);",
            (new_order_id, prod_id, 10)
        )
    
    conn.commit()
    print(f"\nTask 3: Successfully created Order ID {new_order_id} within a transaction.")

    verify_query = """
    SELECT li.line_item_id, li.quantity, p.product_name
    FROM line_items AS li
    JOIN products AS p ON li.product_id = p.product_id
    WHERE li.order_id = ?;
    """
    cursor.execute(verify_query, (new_order_id,))
    verification_results = cursor.fetchall()

    print(f"Line items for Order ID {new_order_id}:")
    
   
    for item in verification_results:
        li_id, qty, prod_name = item
        print(f" - Line Item ID: {li_id} | Product: {prod_name} | Qty: {qty}")

except Exception as e:
    conn.rollback()
    print(f"\nTask 3 Transaction Failed & Rolled Back: {e}")


# Task 4: Aggregation with HAVING

query_task4 = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5;
"""
cursor.execute(query_task4)     
results_task4 = cursor.fetchall()

print("\nTask 4 Results (Employees with > 5 Orders):")
for row in results_task4:
    emp_id, first_name, last_name, order_count = row
   
    print(f"Employee ID: {emp_id} | Name: {first_name} {last_name} | Order Count: {order_count}")

conn.close()