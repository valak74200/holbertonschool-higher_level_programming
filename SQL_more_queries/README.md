# SQL More Queries

This project contains a series of SQL scripts that build upon the basic concepts introduced in SQL_introduction. The scripts cover more advanced SQL topics such as user management, permissions, constraints, joins, and subqueries.

## Description

This project explores more advanced SQL concepts, including:

- User management and privileges
- Constraints (NOT NULL, PRIMARY KEY, FOREIGN KEY, UNIQUE)
- Table relationships (one-to-one, one-to-many, many-to-many)
- JOIN operations (INNER JOIN, LEFT JOIN)
- Subqueries
- Advanced data manipulation and querying

## Requirements

- MySQL 5.7 or higher
- All scripts should be executed on Ubuntu 20.04 LTS
- All files should end with a new line
- All SQL queries should have a comment just before
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)

## Scripts

| Script | Description |
|--------|-------------|
| `0-privileges.sql` | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates the MySQL server user `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege |
| `3-force_name.sql` | Creates a table `force_name` with a NOT NULL constraint |
| `4-never_empty.sql` | Creates a table `id_not_null` with a default value constraint |
| `5-unique_id.sql` | Creates a table `unique_id` with a UNIQUE constraint |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and the table `states` with a PRIMARY KEY constraint |
| `7-cities.sql` | Creates the table `cities` with a FOREIGN KEY constraint referencing the `states` table |
| `8-cities_of_california_subquery.sql` | Lists all cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their state names using a JOIN operation |
| `10-genre_id_by_show.sql` | Lists shows with at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows with their genre IDs (or NULL if no genre) |
| `12-no_genre.sql` | Lists shows without a genre linked |
| `13-count_shows_by_genre.sql` | Lists genres and the number of shows linked to each |
| `14-my_genres.sql` | Lists all genres of the show "Dexter" |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their genres (or NULL if no genre) |

## Database Schema

Several scripts in this project work with a database that contains the following tables:

- `tv_shows`: Contains show information (id, title)
- `tv_genres`: Contains genre information (id, name)
- `tv_show_genres`: Links shows to genres (show_id, genre_id)

## Usage

To execute a script, use the following command:

```bash
$ mysql -hlocalhost -uroot -p < script_name.sql
```

Replace `script_name.sql` with the name of the script you want to run.

## Example

```bash
$ mysql -hlocalhost -uroot -p < 0-privileges.sql
```

This will execute the script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`.

## Learning Objectives

After completing this project, you should be able to:

- Create new MySQL users and manage their privileges
- Understand and implement constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL)
- Use subqueries to retrieve data
- Join tables using different types of JOINs
- Create and manage databases with related tables
- Write complex SQL queries to retrieve and manipulate data
- Understand the concept of database normalization
