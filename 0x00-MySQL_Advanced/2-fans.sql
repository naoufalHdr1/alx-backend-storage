-- Task 2: Rank country origins of bands ordered by the number of (non-unique) fans.
-- This script computes the total number of fans per country and orders the results.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
