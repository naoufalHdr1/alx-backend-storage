-- This SQL script creates a trigger that decreases the quantity of an item
-- in the items table after a new order is added to the orders table.

-- Drop existing trigger if it exists
DROP TRIGGER IF EXISTS decrease_quantity;

-- Create the trigger
DELIMITER //
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table by subtracting the number of items ordered
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //
DELIMITER ;
