-- SQL
SELECT 
    band_name,
    (2024 - formed) AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
