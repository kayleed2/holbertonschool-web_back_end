-- Scriopt that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (split - formed) as lifespan
FROM metal_bands
GROUP BY band_name
ORDER BY lifespan DESC;
 