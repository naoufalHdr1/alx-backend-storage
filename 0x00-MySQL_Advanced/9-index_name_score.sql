-- Task: Create an index on the first letter of the 'name' column and score column in the 'names' table.

-- Create the composite index idx_name_first_score
CREATE INDEX idx_name_first_score ON names (name(1), score);
