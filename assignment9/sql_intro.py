import sqlite3

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
            )
            """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
            """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
            )
            """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            )
            """)
        print("Database created and all tables set up successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")


def add_publisher(cursor, name):

    try:
        cursor.execute("Insert Into publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' is already in the database.")


def add_magazine(cursor, title, publisher_name):
   
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    results = cursor.fetchall()
    if len(results) > 0:
        publisher_id = results[0][0]
    else:
        print(f"Publisher '{publisher_name}' not found.")
        return
    
    try:
        cursor.execute("INSERT INTO magazines (title, publisher_id) VALUES (?, ?)", (title, publisher_id))      
    except sqlite3.IntegrityError:     
        print(f"Magazine '{title}' is already in the database.")
        
def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    results= cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber '{name}' at '{address}' is already in the database.")
        return
    cursor.execute("Insert into subscribers (name, address) Values (?, ?)", (name, address))

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_title, expiration_date):
    cursor.execute("Select subscriber_id From subscribers Where name = ? AND address = ?", (subscriber_name, subscriber_address))
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"Subscriber '{subscriber_name}' not found.")
        return
    cursor.execute("SELECT magazine_id FROM magazines WHERE title = ?", (magazine_title,))
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"Magazine '{magazine_title}' not found.")
        return
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscription for '{subscriber_name}' to '{magazine_title}' already exists.")
        return
    
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        add_publisher(cursor, "Conde Nast")
        add_publisher(cursor, "Hearst")
        add_publisher(cursor, "Dotdash Meredith")

        add_magazine(cursor,"Vogue", "Conde Nast")
        add_magazine(cursor,"Cosmopolitan", "Conde Nast")
        add_magazine(cursor, "People","Dotdash Meredith")

        add_subscriber(cursor, "Alice Smith", "123 Main St")
        add_subscriber(cursor, "Bob Jones", "456 Elm St")
        add_subscriber(cursor, "Charlie Brown", "789 Oak St")

        add_subscription(cursor, "Alice Smith", "123 Main St", "Vogue", "2027-01-01")
        add_subscription(cursor, "Alice Smith", "123 Main St", "Vogue", "2027-06-01")
        add_subscription(cursor, "Alice Smith", "123 Main St", "Vogue", "2027-03-15")
        add_subscription(cursor, "Alice Smith", "123 Main St", "Vogue", "2027-12-31")

        conn.commit()
        print("Data inserted and committed successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")



print("\n--- 1. All Subscribers ---")
cursor.execute("SELECT * From subscribers")
for row in cursor.fetchall():
    print(row)

print("\n--- 2. All Magazines Sorted by Name ---")
cursor.execute("SELECT * FROM magazines ORDER BY title")
for row in cursor.fetchall():
    print(row)

print("\n--- 3. Magazines by Publisher (Conde Nast) ---")
cursor.execute("""
SELECT magazines.title, publishers.name
FROM magazines
JOIN publishers ON magazines.publisher_id = publishers.publisher_id
WHERE publishers.name = 'Conde Nast' 
""")

for row in cursor.fetchall():
    print(row)