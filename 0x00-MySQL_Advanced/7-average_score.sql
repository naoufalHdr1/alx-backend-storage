-- Task: Compute and store the average score for a student.
-- This script creates a stored procedure 'ComputeAverageScoreForUser' that calculates the average score for a student

-- Ensure the procedure doesn't already exist
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;

	-- Calculate the average score for the specified user
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	-- Update the average_score field in the users table for the specified user
	UPDATE users
	SET average_score = IFNULL(avg_score, 0)
	WHERE id = user_id;
END //
DELIMITER ;
