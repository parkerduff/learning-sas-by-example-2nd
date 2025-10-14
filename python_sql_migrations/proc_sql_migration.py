"""
PROC SQL Migration
Python equivalent of SAS PROC SQL from Solutions_to_Odd_Numbered_problems.sas lines 1901-1915
Calculates percentages using calculated fields
"""

import pandas as pd
from load_blood_data import load_blood_data


def proc_sql_percentages(df, n_obs=10):
    """
    Calculate percentages relative to mean for first N observations
    Equivalent to SAS PROC SQL example 26-9
    
    Parameters:
    -----------
    df : pd.DataFrame
        Blood dataset
    n_obs : int
        Number of observations to process (default 10, matching SAS obs=10)
    
    Returns:
    --------
    pd.DataFrame
        Table with Subject, RBC, WBC, MeanRBC, MeanWBC, Percent_RBC, Percent_WBC
    """
    blood_subset = df.head(n_obs).copy()
    
    mean_rbc = blood_subset['RBC'].mean()
    mean_wbc = blood_subset['WBC'].mean()
    
    blood_subset['MeanRBC'] = mean_rbc
    blood_subset['MeanWBC'] = mean_wbc
    blood_subset['Percent_RBC'] = 100 * blood_subset['RBC'] / mean_rbc
    blood_subset['Percent_WBC'] = 100 * blood_subset['WBC'] / mean_wbc
    
    percentages = blood_subset[[
        'Subject', 'RBC', 'WBC', 
        'MeanRBC', 'MeanWBC', 
        'Percent_RBC', 'Percent_WBC'
    ]]
    
    return percentages


def generate_sql_proc_sql():
    """
    Generate SQL equivalent of PROC SQL percentages calculation
    
    Returns:
    --------
    str
        SQL query string
    """
    sql = """
-- PROC SQL equivalent: Calculate percentages relative to mean
-- Using first 10 observations (LIMIT 10)

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
"""
    return sql


if __name__ == '__main__':
    df = load_blood_data()
    
    print("=" * 80)
    print("PROC SQL Migration - Percentages with Calculated Fields")
    print("=" * 80)
    
    percentages = proc_sql_percentages(df)
    print("\nPython Output:")
    print(percentages.to_string(index=False))
    
    print("\n" + "=" * 80)
    print("SQL Equivalent Query:")
    print("=" * 80)
    print(generate_sql_proc_sql())
