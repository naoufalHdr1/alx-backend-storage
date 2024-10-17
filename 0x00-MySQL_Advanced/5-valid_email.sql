-- This SQL script creates a trigger that resets the valid_email attribute
-- in the users table only when the email has been changed.

-- Drop existing trigger if it exists
DROP TRIGGER IF EXISTS reset_valid_email;

-- Create the trigger
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END //
DELIMITER ;
