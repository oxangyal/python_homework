import sqlite3

with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")

        cursor = conn.cursor()

        # Create publishers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            );
        """)
        print("Table publishers is created")

        # Create magazines table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
            );
        """)
        print("Table magazines is created")

        # Create subscribers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            );
        """)
        print("Table subscribers is created")

        # Create subscriptions table
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
