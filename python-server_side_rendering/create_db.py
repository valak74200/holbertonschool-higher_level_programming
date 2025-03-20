#!/usr/bin/env python3
"""
Script to create and populate the SQLite database for the Flask application.
"""
import sqlite3

def create_database():
    """Create and populate the SQLite database with product data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear existing data to avoid duplicates on re-run
    cursor.execute('DELETE FROM Products')
    
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Headphones', 'Electronics', 149.99),
        (4, 'Desk Lamp', 'Home Goods', 29.99),
        (5, 'Smartphone', 'Electronics', 699.99)
    ''')
    conn.commit()
    conn.close()
    print("Database created and populated successfully.")

if __name__ == '__main__':
    create_database()
