
SELECT 
    Gender,
    BloodType,
    ROUND(AVG(CASE WHEN AgeGroup = 'Old' THEN WBC END), 0) as Old_WBC,
    ROUND(AVG(CASE WHEN AgeGroup = 'Young' THEN WBC END), 0) as Young_WBC,
    ROUND(AVG(CASE WHEN AgeGroup = 'Old' THEN RBC END), 2) as Old_RBC,
    ROUND(AVG(CASE WHEN AgeGroup = 'Young' THEN RBC END), 2) as Young_RBC
FROM blood
GROUP BY Gender, BloodType
ORDER BY Gender, BloodType;
