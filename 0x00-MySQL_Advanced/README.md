# 0x00. MySQL Advanced
`#Back-end` `#SQL` `#MySQL`

## Description

This project focuses on advanced SQL features such as creating tables with constraints, optimizing queries using indexes, implementing stored procedures and functions, creating views, and using triggers in MySQL. These concepts are essential for managing and optimizing databases in backend development, ensuring data integrity, and improving query performance.

## Learning Objectives

By the end of this project, you should be able to:

1. **Create Tables with Constraints:** Learn how to define primary keys, unique constraints, and foreign keys when creating tables.
2. **Optimize Queries with Indexes:** Understand how indexes improve query performance and how to implement them.
3. **Implement Stored Procedures and Functions:** Use MySQL stored procedures and functions to encapsulate logic and reuse code.
4. **Work with Views:** Learn how to create views to simplify complex queries and enhance data security.
5. **Implement Triggers:** Understand how to use triggers to automate actions in response to database events.

## Project Structure

The project consists of several SQL scripts designed to demonstrate the implementation of these advanced MySQL concepts. Each script follows the guidelines provided, with comments explaining the purpose and SQL commands used.

## Requirements

- All scripts are compatible with **MySQL 5.7**.
- Each file starts with comments describing the task.
- SQL keywords are written in uppercase (e.g., `SELECT`, `WHERE`).
- Scripts must not fail if tables already exist.

## Setup Instructions

To run the SQL scripts in this project:

1. Start the MySQL service in your container:
```bash
service mysql start
```

2. Execute the SQL scripts using the MySQL command-line interface:
```bash
mysql -uroot -p
```

3. You can import and test each script using:
```bash
mysql -uroot -p < script_name.sql
```

## Usage Example

To execute the `0-uniq_users.sql` script:
```bash
$ mysql -uroot -p
Enter password:
mysql> source 0-uniq_users.sql;
```

## How to Import a SQL Dump

For tasks requiring data imports, such as the metal bands data:
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```
