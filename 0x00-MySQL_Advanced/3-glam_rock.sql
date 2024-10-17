-- Task 3: List all bands with Glam rock as their main style, ranked by their longevity.
-- This script computes the lifespan of bands based on their formation year until 2022.

SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan DESC;
