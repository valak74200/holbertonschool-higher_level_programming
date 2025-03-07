# Python Object-Relational Mapping (ORM)

This project explores the connection between databases and Python through Object-Relational Mapping (ORM). It demonstrates two approaches to connecting to a MySQL database from Python:

1. Using the `MySQLdb` module to execute direct SQL queries
2. Using the `SQLAlchemy` ORM to abstract the storage layer

## Description

Object-Relational Mapping (ORM) is a programming technique that converts data between incompatible type systems in object-oriented programming languages. This project demonstrates how to:

- Connect to a MySQL database from a Python script
- Execute SQL queries to create, read, update, and delete data
- Use SQLAlchemy ORM to abstract database operations
- Define models that map to database tables
- Establish relationships between models

## Requirements

- Python 3.8.5 or higher
- MySQL 5.7 or higher
- MySQLdb module version 2.0.x
- SQLAlchemy module version 1.4.x
- All files should be executable
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Code should follow PEP 8 style guidelines

## Installation

```bash
# Install MySQLdb
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient

# Install SQLAlchemy
$ sudo pip3 install SQLAlchemy
```

## Scripts

### Direct SQL Queries with MySQLdb

| Script | Description |
|--------|-------------|
| `0-select_states.py` | Lists all states from the database `hbtn_0e_0_usa` |
| `0-select_states.sql` | Creates the states table in `hbtn_0e_0_usa` with sample data |
| `1-filter_states.py` | Lists all states with a name starting with 'N' |
| `2-my_filter_states.py` | Lists all states where name matches an argument |
| `3-my_safe_filter_states.py` | Lists all states where name matches an argument (safe from SQL injection) |
| `4-cities_by_state.py` | Lists all cities from the database |
| `4-cities_by_state.sql` | Creates the cities table in `hbtn_0e_4_usa` with sample data |
| `5-filter_cities.py` | Lists all cities of a state |

### ORM with SQLAlchemy

| Script | Description |
|--------|-------------|
| `model_state.py` | Contains the class definition of a State and an instance Base = declarative_base() |
| `6-model_state.sql` | Creates the database `hbtn_0e_6_usa` with the states table |
| `7-model_state_fetch_all.py` | Lists all State objects from the database |
| `7-model_state_fetch_all.sql` | Inserts states into `hbtn_0e_6_usa` |
| `8-model_state_fetch_first.py` | Prints the first State object from the database |
| `9-model_state_filter_a.py` | Lists all State objects that contain the letter 'a' |
| `10-model_state_my_get.py` | Prints the State object with the name passed as argument |
| `11-model_state_insert.py` | Adds the State object "Louisiana" to the database |
| `12-model_state_update_id_2.py` | Changes the name of a State object in the database |
| `13-model_state_delete_a.py` | Deletes all State objects with a name containing the letter 'a' |
| `model_city.py` | Contains the class definition of a City, which inherits from Base |
| `14-model_city_fetch_by_state.py` | Prints all City objects from the database |
| `14-model_city_fetch_by_state.sql` | Creates the database `hbtn_0e_14_usa` with tables states and cities |

## Usage

### Direct SQL Queries with MySQLdb

```bash
$ ./0-select_states.py username password database_name
```

### ORM with SQLAlchemy

```bash
$ ./7-model_state_fetch_all.py username password database_name
```

## Example

```bash
$ cat 0-select_states.sql | mysql -uroot -p
$ ./0-select_states.py root root_passwd hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

## Learning Objectives

After completing this project, you should be able to:

- Connect to a MySQL database from a Python script
- Execute SQL queries on a MySQL database from a Python script
- Map a Python class to a MySQL table using an ORM
- Create a Python Virtual Environment
- Understand the concept of Object-Relational Mapping
- Prevent SQL injection attacks
- Create, read, update, and delete records in a database using Python
