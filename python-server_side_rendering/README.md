# Python Server-Side Rendering 🖥️

This project explores server-side rendering techniques in Python, focusing on template engines, data processing, and web application development with Flask.

## 📋 Project Overview

Server-side rendering (SSR) is a technique where web pages are generated on the server before being sent to the client. This project demonstrates various approaches to SSR in Python, from basic string templating to more advanced techniques using Flask and Jinja2.

## 🧩 Project Components

### 1. Basic Template Rendering (`task_00_intro.py`)
- Simple string template replacement
- Generating invitation files from a template and attendee data
- Error handling and validation

### 2. Flask with Jinja2 Templates (`task_01_jinja.py`)
- Basic Flask application setup
- Route definitions
- Simple page rendering with Jinja2 templates

### 3. Template Logic (`task_02_logic.py`)
- Using loops and conditionals in Jinja2 templates
- Reading data from JSON files
- Dynamic content rendering

### 4. File Handling (`task_03_files.py`)
- Reading and processing data from different file formats (JSON, CSV)
- Query parameter handling
- Filtering and displaying product data

### 5. Database Integration (`task_04_db.py`)
- SQLite database connection
- Reading and filtering data from a database
- Combining multiple data sources (JSON, CSV, SQLite)

## 🛠️ Technologies Used
- Python 3
- Flask (Web framework)
- Jinja2 (Template engine)
- SQLite (Database)
- JSON and CSV file processing

## 📁 File Structure
```
python-server_side_rendering/
├── create_db.py              # Script to create the SQLite database
├── items.json                # Sample JSON data for items
├── main.py                   # Main test file
├── output_*.txt              # Generated output files
├── products.csv              # Sample CSV data
├── products.db               # SQLite database
├── products.json             # Sample JSON data for products
├── task_00_intro.py          # Basic template rendering
├── task_01_jinja.py          # Flask with Jinja2 templates
├── task_02_logic.py          # Template logic
├── task_03_files.py          # File handling
├── task_04_db.py             # Database integration
├── template.txt              # Template file for task_00
└── templates/                # Directory containing HTML templates
    ├── about.html
    ├── contact.html
    ├── index.html
    ├── items.html
    └── product_display.html
```

## 🚀 Usage

### Basic Template Rendering
```bash
python3 task_00_intro.py
```

### Flask Applications
```bash
# Run the basic Flask app
python3 task_01_jinja.py

# Run the Flask app with template logic
python3 task_02_logic.py

# Run the Flask app with file handling
python3 task_03_files.py

# Run the Flask app with database integration
python3 task_04_db.py
```

### Accessing the Web Applications
- Home page: http://localhost:5000/
- About page: http://localhost:5000/about
- Contact page: http://localhost:5000/contact
- Items page: http://localhost:5000/items
- Products page: 
  - JSON source: http://localhost:5000/products?source=json
  - CSV source: http://localhost:5000/products?source=csv
  - SQL source: http://localhost:5000/products?source=sql
  - Filter by ID: http://localhost:5000/products?source=json&id=1

## 📚 Learning Objectives
- Understand server-side rendering concepts
- Implement template engines in Python
- Process data from various sources (JSON, CSV, databases)
- Build dynamic web applications with Flask
- Use Jinja2 for template logic and rendering

## 🔍 Key Concepts
- **Server-Side Rendering**: Generating HTML on the server before sending to the client
- **Template Engines**: Tools that combine templates with data to produce documents
- **Jinja2**: A modern and designer-friendly templating language for Python
- **Flask**: A lightweight WSGI web application framework
- **Data Processing**: Reading and manipulating data from various sources
