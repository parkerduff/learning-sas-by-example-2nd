
SELECT 
    'RBC' as Variable,
    COUNT(RBC) as N,
    COUNT(*) - COUNT(RBC) as N_Miss,
    ROUND(AVG(RBC), 1) as Mean,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY RBC), 1) as Median,
    ROUND(MIN(RBC), 1) as Min,
    ROUND(MAX(RBC), 1) as Max
FROM blood

UNION ALL

SELECT 
    'WBC' as Variable,
    COUNT(WBC) as N,
    COUNT(*) - COUNT(WBC) as N_Miss,
    ROUND(AVG(WBC), 1) as Mean,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY WBC), 1) as Median,
    ROUND(MIN(WBC), 1) as Min,
    ROUND(MAX(WBC), 1) as Max
FROM blood
ORDER BY Variable;
