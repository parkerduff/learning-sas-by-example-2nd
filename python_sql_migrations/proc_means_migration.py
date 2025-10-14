"""
PROC MEANS Migration
Python equivalent of SAS PROC MEANS from Programs Used in the Second Edition.sas lines 2176-2185
"""

import pandas as pd
from load_blood_data import load_blood_data


def proc_means(df, variables=['RBC', 'WBC'], maxdec=1):
    """
    Calculate statistics similar to SAS PROC MEANS
    
    Parameters:
    -----------
    df : pd.DataFrame
        Blood dataset
    variables : list
        List of variable names to analyze
    maxdec : int
        Maximum decimal places (default 1)
    
    Returns:
    --------
    pd.DataFrame
        Statistics table with columns: Variable, N, N_Miss, Mean, Median, Min, Max
    """
    results = []
    
    for var in variables:
        series = df[var]
        stats_dict = {
            'Variable': var,
            'N': series.count(),
            'N_Miss': series.isna().sum(),
            'Mean': series.mean(),
            'Median': series.median(),
            'Min': series.min(),
            'Max': series.max()
        }
        results.append(stats_dict)
    
    stats = pd.DataFrame(results)
    
    stats['Mean'] = stats['Mean'].round(maxdec)
    stats['Median'] = stats['Median'].round(maxdec)
    stats['Min'] = stats['Min'].round(maxdec)
    stats['Max'] = stats['Max'].round(maxdec)
    
    stats['N'] = stats['N'].astype(int)
    stats['N_Miss'] = stats['N_Miss'].astype(int)
    
    return stats


if __name__ == '__main__':
    df = load_blood_data()
    
    print("=" * 60)
    print("PROC MEANS Migration - Selected Statistics")
    print("=" * 60)
    
    stats = proc_means(df)
    print("\nPython Output:")
    print(stats.to_string(index=False))
    
    print("\n" + "=" * 60)
    print("SQL Equivalent: See proc_means.sql")
    print("=" * 60)
