-- Task 0: Create a 'users' table with the following specifications:
-- - The 'id' column is an auto-incrementing integer that serves as the primary key.
-- - The 'email' column is a string (VARCHAR) that cannot be null and must be unique.
-- - The 'name' column is a string (VARCHAR) that can store the user's name, allowing null values.
-- - The script should not fail if the table already exists.

-- Check if the 'users' table exists and create it if it doesn't
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
);
