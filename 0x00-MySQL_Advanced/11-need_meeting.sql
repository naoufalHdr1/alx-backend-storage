-- Task: Create a view 'need_meeting' to list students with score under 80 and no recent meeting

-- Drop the view if it already exists to avoid conflicts
DROP VIEW IF EXISTS need_meeting;

-- Create the view
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
