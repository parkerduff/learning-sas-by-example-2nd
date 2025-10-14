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


if __name__ == '__main__':
    df = load_blood_data()
    
    print("=" * 80)
    print("PROC SQL Migration - Percentages with Calculated Fields")
    print("=" * 80)
    
    percentages = proc_sql_percentages(df)
    print("\nPython Output:")
    print(percentages.to_string(index=False))
    
    print("\n" + "=" * 80)
    print("SQL Equivalent: See proc_sql.sql")
    print("=" * 80)
