-- Task: create the stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	DECLARE current_id INT DEFAULT 1; -- Start from the first user
	DECLARE total_users INT;
	DECLARE total_weight INT DEFAULT 0;
	DECLARE weighted_score_sum FLOAT DEFAULT 0;

	-- Get the total number of users
	SELECT COUNT(*) INTO total_users FROM users;

	-- Loop through all users
	WHILE current_id <= total_users DO
		-- Calculate total weight for the current user
		SELECT SUM(p.weight)
		INTO total_weight
		FROM corrections c
		JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = current_id;

		-- Calculate weighted score for the current user
		SELECT SUM(c.score * p.weight)
		INTO weighted_score_sum
		FROM corrections c
		JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = current_id;

		-- Update the user's average score based on the calculated weighted average
		IF total_weight > 0 THEN
			UPDATE users
			SET average_score = weighted_score_sum / total_weight
			WHERE id = current_id;
		    ELSE
        		UPDATE users
			SET average_score = 0
			WHERE id = current_id;
		END IF;
		
		-- Increment the current_id to process the next user
		SET current_id = current_id + 1;
	END WHILE;
END //
DELIMITER ;
