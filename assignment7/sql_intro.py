import sqlite3


def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
        print(f"Publisher: {name}")
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        print(f"Populated magazine: {name}")
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists or invalid publisher_id")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?, ?)", (name, address))
        print(f"Populated subscriber: {name}, address: {address}")
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' with address '{address}' already exists")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                       (subscriber_id, magazine_id, expiration_date))
        print(f"Populated subscription: subscriber_id={subscriber_id}, magazine_id={magazine_id}")
    except sqlite3.IntegrityError:
        print(f"Subscription for subscriber_id={subscriber_id} and magazine_id={magazine_id} already exists")

with sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully.")
    conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
    """)
    print("Table publishers is created")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        );
    """)
    print("Table magazines is created")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE (name, address)
        );
    """)
    print("Table subscribers is created")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines( magazine_id),
            UNIQUE (subscriber_id, magazine_id)
        );
    """)
    print("Table subscriptions is created")
    print("All tables created successfully:")

    # Populate data
    add_publisher(cursor, 'Hearst Communications')
    add_publisher(cursor, 'National Geographic')
    add_publisher(cursor, 'Scholastic Inc')

    add_magazine(cursor, 'Popular Mechanics', 1)
    add_magazine(cursor, 'Seventeen', 1)
    add_magazine(cursor, 'National Geographic', 2)
    add_magazine(cursor, 'National Geographic Kids', 2)
    add_magazine(cursor, 'Scholastic News', 3)
    add_magazine(cursor, 'Storyworks', 3)

    subscribers = [
        ("Alex Johnson", "110 Commonwealth Ave, Boston, MA"),
        ("Maria Hill", "568 Main Street, Concord, MA"),
        ("George McDonald", "87 Beach Ln, St. Augustine, FL")
    ]
    for name, address in subscribers:
        add_subscriber(cursor, name, address)

    subscriptions = [
        (1, 1, "2025-12-31"),
        (1, 2, "2025-06-30"),
        (2, 2, "2025-09-30"),
        (3, 3, "2026-01-31")
    ]
    for subscriber_id, magazine_id, expiration_date in subscriptions:
        add_subscription(cursor, subscriber_id, magazine_id, expiration_date)

    # Commit changes
    conn.commit()
    print("Data populated and committed successfully")
