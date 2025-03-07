# SQL Introduction

This project contains a series of SQL scripts that introduce the fundamental concepts of SQL (Structured Query Language). The scripts progress from basic database operations to more complex queries, providing a comprehensive introduction to SQL.

## Description

SQL (Structured Query Language) is a domain-specific language used for managing and manipulating relational databases. This project covers the basics of SQL, including:

- Creating and deleting databases
- Creating tables
- Inserting and modifying data
- Querying data with SELECT statements
- Filtering data with WHERE clauses
- Sorting data with ORDER BY
- Aggregating data with GROUP BY and functions like COUNT, AVG, etc.

## Requirements

- MySQL 5.7 or higher
- All scripts should be executed on Ubuntu 20.04 LTS
- All files should end with a new line
- All SQL queries should have a comment just before
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)

## Scripts

| Script | Description |
|--------|-------------|
| `0-list_databases.sql` | Lists all databases on the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't already exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables in a specified database |
| `4-first_table.sql` | Creates a table called `first_table` with columns `id` (INT) and `name` (VARCHAR(256)) |
| `5-full_table.sql` | Prints the full description of the `first_table` |
| `6-list_values.sql` | Lists all rows in the `first_table` |
| `7-insert_value.sql` | Inserts a new row into the `first_table` |
| `8-count_89.sql` | Displays the number of records with `id = 89` in the `first_table` |
| `9-full_creation.sql` | Creates a table called `second_table` and adds multiple rows |
| `10-top_score.sql` | Lists all records of the `second_table` ordered by score (top first) |
| `11-best_score.sql` | Lists all records with a score >= 10 in the `second_table` |
| `12-no_cheating.sql` | Updates the score of Bob to 10 in the `second_table` |
| `13-change_class.sql` | Removes all records with a score <= 5 in the `second_table` |
| `14-average.sql` | Computes the average score of all records in the `second_table` |
| `15-groups.sql` | Lists the number of records with the same score in the `second_table` |
| `16-no_link.sql` | Lists all records of the `second_table` where name is not empty, ordered by score |

## Usage

To execute a script, use the following command:

```bash
$ mysql -hlocalhost -uroot -p < script_name.sql
```

Replace `script_name.sql` with the name of the script you want to run.

## Example

```bash
$ mysql -hlocalhost -uroot -p < 0-list_databases.sql
```

This will execute the script that lists all databases on the MySQL server.

## Learning Objectives

After completing this project, you should be able to:

- Explain what a database is
- Explain what a relational database is
- Explain what SQL stands for and what it's used for
- Create a database in MySQL
- Perform basic SQL operations: SELECT, INSERT, UPDATE, DELETE
- Use MySQL functions
- Understand and use subqueries
- Create and manipulate tables with SQL
