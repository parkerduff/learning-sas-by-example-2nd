"""
PROC REPORT Migration
Python equivalent of SAS PROC REPORT from Programs Used in the Second Edition.sas lines 2163-2171
"""

import pandas as pd
from load_blood_data import load_blood_data


def proc_report(df):
    """
    Create cross-tabulation report similar to SAS PROC REPORT
    Average Blood Counts by Gender, BloodType, and AgeGroup
    
    Parameters:
    -----------
    df : pd.DataFrame
        Blood dataset
    
    Returns:
    --------
    pd.DataFrame
        Report table with Gender and BloodType as rows, 
        AgeGroup × Measure (WBC, RBC) as columns
    """
    report = df.pivot_table(
        values=['WBC', 'RBC'],
        index=['Gender', 'BloodType'],
        columns='AgeGroup',
        aggfunc='mean'
    )
    
    report.columns = [f'{age}_{measure}' for measure, age in report.columns]
    report = report.reset_index()
    
    column_order = ['Gender', 'BloodType', 'Old_WBC', 'Young_WBC', 'Old_RBC', 'Young_RBC']
    report = report[column_order]
    
    report['Old_WBC'] = report['Old_WBC'].round(0)
    report['Young_WBC'] = report['Young_WBC'].round(0)
    
    report['Old_RBC'] = report['Old_RBC'].round(2)
    report['Young_RBC'] = report['Young_RBC'].round(2)
    
    return report


if __name__ == '__main__':
    df = load_blood_data()
    
    print("=" * 80)
    print("PROC REPORT Migration - Average Blood Counts by Age Group")
    print("=" * 80)
    
    report = proc_report(df)
    print("\nPython Output:")
    print(report.to_string(index=False))
    
    print("\n" + "=" * 80)
    print("SQL Equivalent: See proc_report.sql")
    print("=" * 80)
