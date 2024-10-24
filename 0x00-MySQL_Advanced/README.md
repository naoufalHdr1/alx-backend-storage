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

## Tasks

### Task 0: We are all unique!

Create a SQL script to define a users table with:

- `id`: integer, primary key, auto-increment.
- `email`: string, unique, not null.
- `name`: string.

Ensure the table won't be recreated if it exists.

**File**: `0-uniq_users.sql`

### Task 1: In and not out

Create a SQL script to define a users table with the following attributes:

- `id`: integer, primary key, auto-increment.
- `email`: string (255 characters), unique, not null.
- `name`: string (255 characters).
- `country`: enumeration (US, CO, TN), not null (default is US).

Ensure the table won't be recreated if it exists.

**File**: `1-country_users.sql`

### Task 2: Best band ever!

Create a SQL script that ranks the origins of metal bands based on the number of non-unique fans. The script should:

1. Import the data from the [`metal_bands.sql.zip`](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ) file.
2. Output the results in a table with the columns:
    - `origin`
    - `nb_fans`

The output should be ordered by the number of fans in descending order. Ensure that the script can be executed on any database.

**File**: `2-fans.sql`

### Task 3: Old school band

Create a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity. The script should:

1. Import data from the [`metal_bands.sql.zip`](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ) file.
2. Include the following columns in the output:
    - `band_name`
    - `lifespan` (calculated as the number of years from the band's formation until 2022).

Ensure that the lifespan is computed using the band's formation year, and the script should be executable on any database.

**File**: `3-glam_rock.sql`

### Task 4: Buy buy buy

Create a SQL script that defines a trigger to decrease the `quantity` of an item in the `items` table whenever a new order is added to the `orders` table. The script should:

1. Define the `items` table with `name` (string) and `quantity` (integer).
2. Define the `orders` table with `item_name` (string) and `number` (integer).
3. Implement a trigger to update the `quantity` based on the `number` of items ordered, allowing negative quantities.

Ensure the script is executable on any database.

**File**: `4-store.sql`

### Task 5: Email validation to sent

Write a SQL script that creates a trigger to reset the `valid_email` attribute only when the `email` has been changed. The script should:

1. Define the `users` table with the following columns:
    - `id` (integer, auto-increment, primary key)
    - `email` (string, not null)
    - `name` (string)
    - `valid_email` (boolean, not null, default 0)
2. Insert initial data into the `users` table.
3. Implement a trigger that sets `valid_email` to 0 when the `email` is updated.

Ensure the script is executable on any database.

**File**: `5-valid_email.sql`

### Task 6: Add bonus

Write a SQL script that creates a stored procedure `AddBonus` to add a correction for a student. The procedure should:

- Accept 3 inputs: `user_id` (linked to an existing user), `project_name` (either existing or new), and `score` (integer value).
- Check if the project exists in the `projects` table. If not, create the new project.
- Insert a new correction into the `corrections` table with the provided score for the corresponding user and project.

Ensure the script is executable on any database.

**File**: `6-bonus.sql`

### Task 7: Average Score

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student. The procedure should:

- Accept 1 input: `user_id` (linked to an existing user).
- Calculate the average score from the `corrections` table for the given user.
- Update the `average_score` field in the `users` table with the calculated average.
Ensure the script is executable on any database.

**File**: `7-average_score.sql`

### Task 8: Optimize simple search

Write a SQL script that creates an index `idx_name_first` on the `names` table, indexing only the first letter of the `name` column. The script should:

- Use an index on the first letter of the `name` field.
- Optimize searches for names that start with a specific letter, such as `LIKE 'a%'`.

Ensure the script is executable on any database and improves query performance for searches starting with a letter.

**File**: `8-index_my_names.sql`

### Task 9: Optimize search and score

Write a SQL script that creates an index `idx_name_first_score` on the `names` table, indexing the first letter of the `name` column and the `score` column. The script should:

- Use a compound index on the first letter of the `name` field and the `score`.
- Optimize searches for names starting with a specific letter and filtering by score, such as `LIKE 'a%' AND score < 80`.

Ensure the script is executable on any database and improves query performance for combined searches on name and score.

**File**: `9-index_name_score.sql`

### Task 10: Safe divide

Write a SQL script that creates a function `SafeDiv` which divides two integers and returns the result. If the divisor is zero, the function should return 0. The script should:

- Create the function `SafeDiv` that accepts two arguments:
    - `a`, INT (the numerator)
    - `b`, INT (the divisor)
- Return the result of `a / b` or 0 if `b == 0`.

Ensure the function works with any database and handles edge cases where division by zero may occur.

**File**: 10-div.sql

### Task 11: No table for a meeting

Write a SQL script to create a view called `need_meeting`, listing all students who meet the following criteria:

- Have a score strictly less than 80.
- Either have no `last_meeting` date or had their last meeting more than one month ago.

**File**: `11-need_meeting.sql`

### Task 12 : Average weighted score `#advanced`

Write a SQL script to create a stored procedure `ComputeAverageWeightedScoreForUser` that computes the average weighted score for a student. The procedure should:

- Accept one input, `user_id`, which is linked to the `users.id`.
- Calculate the weighted average score based on each project's score and weight.
- Update the student's `average_score` in the `users` table.

This requires combining data from the `users`, `projects`, and `corrections` tables to compute the weighted average. 

**File**: `100-average_weighted_score.sql`

### Task 13: Average weighted score for all! `#advanced`

Write a SQL script to create a stored procedure named `ComputeAverageWeightedScoreForUsers` that calculates and stores the average weighted score for all students without requiring any input parameters.

**Requirements:**

The procedure should compute the average weighted score for each student based on their scores and the weights of the projects associated with them.
It should update the `average_score` field in the `users` table for each student after the calculation.

**Tips:**

Utilize the formula for calculating a weighted average, combining data from the `users`, `projects`, and `corrections` tables.

**File**: `101-average_weighted_score.sql`
