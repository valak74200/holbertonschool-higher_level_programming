# Python Serialization

This project explores different serialization techniques in Python, including JSON, Pickle, CSV, and XML formats. Each task focuses on a specific serialization method and its implementation.

## Tasks

### Task 0: Basic JSON Serialization
File: `task_00_basic_serialization.py`

This task implements basic JSON serialization and deserialization using Python's `json` module. It includes two functions:
- `serialize_and_save_to_file(data, filename)`: Serializes a Python dictionary to a JSON file
- `load_and_deserialize(filename)`: Loads and deserializes data from a JSON file back into a Python dictionary

### Task 1: Object Serialization with Pickle
File: `task_01_pickle.py`

This task implements object serialization using Python's `pickle` module. It includes a `CustomObject` class with the following features:
- Initialization with name, age, and student status
- `display()` method to show object attributes
- `serialize(filename)` method to save the object to a file
- `deserialize(filename)` class method to load an object from a file

### Task 2: CSV to JSON Conversion
File: `task_02_csv.py`

This task focuses on converting CSV data to JSON format. It includes the function:
- `convert_csv_to_json(csv_filename)`: Reads a CSV file, converts each row into a dictionary, and saves the result as a JSON file named 'data.json'
- Handles file not found and other potential errors
- Returns True on successful conversion, False otherwise

### Task 3: XML Serialization
File: `task_03_xml.py`

This task implements XML serialization using Python's `xml.etree.ElementTree` module. It includes two functions:
- `serialize_to_xml(dictionary, filename)`: Converts a Python dictionary to XML format and saves it to a file
- `deserialize_from_xml(filename)`: Reads an XML file and converts it back to a Python dictionary

## Requirements
- Python 3.x
- No external libraries required (all modules used are part of Python's standard library)

## Usage Examples

### JSON Serialization
```python
data = {"name": "John", "age": 30}
serialize_and_save_to_file(data, "person.json")
loaded_data = load_and_deserialize("person.json")
```

### Pickle Serialization
```python
obj = CustomObject("Alice", 25, True)
obj.serialize("person.pkl")
loaded_obj = CustomObject.deserialize("person.pkl")
loaded_obj.display()
```

### CSV to JSON Conversion
```python
success = convert_csv_to_json("input.csv")
if success:
    print("Conversion completed successfully")
```

### XML Serialization
```python
data = {"name": "Bob", "age": "35"}
serialize_to_xml(data, "person.xml")
loaded_data = deserialize_from_xml("person.xml")
