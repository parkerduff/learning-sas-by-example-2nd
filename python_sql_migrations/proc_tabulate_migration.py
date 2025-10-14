"""
PROC TABULATE Migration
Python equivalent of SAS PROC TABULATE from Programs Used in the Second Edition.sas lines 2492-2534
Multiple examples (18-4 through 18-9)
"""

import pandas as pd
from load_blood_data import load_blood_data


def tabulate_18_4(df):
    """
    Example 18-4: Demonstrating Nesting
    Gender × BloodType frequency counts
    """
    tab = pd.crosstab(
        df['Gender'], 
        df['BloodType']
    )
    return tab


def tabulate_18_5(df):
    """
    Example 18-5: Adding the Keyword ALL to the TABLE Request
    Gender × BloodType with row and column totals
    """
    tab = pd.crosstab(
        df['Gender'], 
        df['BloodType'],
        margins=True,
        margins_name='ALL'
    )
    return tab


def tabulate_18_8(df):
    """
    Example 18-8: Specifying More than One Statistic
    Mean, Min, Max for RBC and WBC
    """
    stats_table = df[['RBC', 'WBC']].agg(['mean', 'min', 'max'])
    stats_table = stats_table.round(2)
    stats_table = stats_table.T
    return stats_table


def tabulate_18_9(df):
    """
    Example 18-9: Combining CLASS and Analysis Variables
    Mean of RBC, WBC, Chol by Gender × AgeGroup with totals
    """
    tab = df.pivot_table(
        values=['RBC', 'WBC', 'Chol'],
        index='Gender',
        columns='AgeGroup',
        aggfunc='mean',
        margins=True,
        margins_name='All'
    )
    tab = tab.round(2)
    return tab


if __name__ == '__main__':
    df = load_blood_data()
    
    print("=" * 80)
    print("PROC TABULATE Migrations")
    print("=" * 80)
    
    print("\n" + "=" * 80)
    print("Example 18-4: Gender × BloodType Nesting (Frequency Counts)")
    print("=" * 80)
    tab_4 = tabulate_18_4(df)
    print(tab_4)
    
    print("\n" + "=" * 80)
    print("Example 18-5: With ALL Keyword (Row and Column Totals)")
    print("=" * 80)
    tab_5 = tabulate_18_5(df)
    print(tab_5)
    
    print("\n" + "=" * 80)
    print("Example 18-8: Multiple Statistics (Mean, Min, Max)")
    print("=" * 80)
    tab_8 = tabulate_18_8(df)
    print(tab_8)
    
    print("\n" + "=" * 80)
    print("Example 18-9: CLASS + Analysis Variables (Gender × AgeGroup)")
    print("=" * 80)
    tab_9 = tabulate_18_9(df)
    print(tab_9)
    
    print("\n" + "=" * 80)
    print("SQL Equivalents: See proc_tabulate.sql")
    print("=" * 80)
