#!/usr/bin/env python3
"""
A Flask application that reads and displays product data from different file formats.
"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read and parse the JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv_file():
    """Read and parse the CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric values
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    # Skip rows with invalid numeric values
                    continue
                products.append(row)
        return products
    except FileNotFoundError as e:
        print(f"Error reading CSV file: {e}")
        return []


@app.route('/')
def home():
    """Route for the home page."""
    return render_template('index.html')


@app.route('/products')
def products():
    """
    Route for displaying products from different file sources.
    
    Query parameters:
    - source: The data source (json or csv)
    - id: Optional product ID to filter by
    """
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Convert product_id to integer if provided
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', 
                                  error="Invalid product ID format")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_file()
    elif source == 'csv':
        products_data = read_csv_file()
    else:
        return render_template('product_display.html', 
                              error="Wrong source")
    
    # Filter by ID if provided
    if product_id:
        filtered_products = [p for p in products_data if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html', 
                                  error="Product not found")
        products_data = filtered_products
    
    # Render the template with the products
    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
