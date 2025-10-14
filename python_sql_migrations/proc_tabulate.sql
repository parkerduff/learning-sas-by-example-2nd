
SELECT 
    Gender,
    SUM(CASE WHEN BloodType = 'A' THEN 1 ELSE 0 END) as A,
    SUM(CASE WHEN BloodType = 'AB' THEN 1 ELSE 0 END) as AB,
    SUM(CASE WHEN BloodType = 'B' THEN 1 ELSE 0 END) as B,
    SUM(CASE WHEN BloodType = 'O' THEN 1 ELSE 0 END) as O
FROM blood
GROUP BY Gender
ORDER BY Gender;

SELECT 
    COALESCE(Gender, 'ALL') as Gender,
    SUM(CASE WHEN BloodType = 'A' THEN 1 ELSE 0 END) as A,
    SUM(CASE WHEN BloodType = 'AB' THEN 1 ELSE 0 END) as AB,
    SUM(CASE WHEN BloodType = 'B' THEN 1 ELSE 0 END) as B,
    SUM(CASE WHEN BloodType = 'O' THEN 1 ELSE 0 END) as O,
    COUNT(*) as ALL_total
FROM blood
GROUP BY ROLLUP(Gender)
ORDER BY 
    CASE WHEN Gender IS NULL THEN 1 ELSE 0 END,
    Gender;

SELECT 
    'RBC' as Variable,
    ROUND(AVG(RBC), 2) as Mean,
    ROUND(MIN(RBC), 2) as Min,
    ROUND(MAX(RBC), 2) as Max
FROM blood
UNION ALL
SELECT 
    'WBC' as Variable,
    ROUND(AVG(WBC), 2) as Mean,
    ROUND(MIN(WBC), 2) as Min,
    ROUND(MAX(WBC), 2) as Max
FROM blood
ORDER BY Variable;

SELECT 
    COALESCE(Gender, 'All') as Gender,
    COALESCE(AgeGroup, 'All') as AgeGroup,
    ROUND(AVG(RBC), 2) as Mean_RBC,
    ROUND(AVG(WBC), 2) as Mean_WBC,
    ROUND(AVG(Chol), 2) as Mean_Chol
FROM blood
GROUP BY ROLLUP(Gender, AgeGroup)
ORDER BY 
    CASE WHEN Gender IS NULL THEN 1 ELSE 0 END,
    Gender,
    CASE WHEN AgeGroup IS NULL THEN 1 ELSE 0 END,
    AgeGroup;
