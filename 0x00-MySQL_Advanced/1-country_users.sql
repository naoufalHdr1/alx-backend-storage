-- Task: Create a 'users' table with specific attributes including email, name, and country.
-- The country field is an enumeration with allowed values: US, CO, and TN.
-- This script will not fail if the table already exists.

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY (id)
);
