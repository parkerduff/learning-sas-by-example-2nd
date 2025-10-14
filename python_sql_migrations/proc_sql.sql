
WITH first_10 AS (
    SELECT * FROM blood LIMIT 10
),
means AS (
    SELECT 
        AVG(RBC) as MeanRBC,
        AVG(WBC) as MeanWBC
    FROM first_10
)
SELECT 
    f.Subject,
    f.RBC,
    f.WBC,
    m.MeanRBC,
    m.MeanWBC,
    100 * f.RBC / m.MeanRBC as Percent_RBC,
    100 * f.WBC / m.MeanWBC as Percent_WBC
FROM first_10 f
CROSS JOIN means m
ORDER BY f.Subject;
