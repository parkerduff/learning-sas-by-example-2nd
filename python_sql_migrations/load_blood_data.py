"""
Blood Dataset Loader
Loads the blood.txt data file into a pandas DataFrame
Equivalent to SAS DATA step from Create_Datasets.sas lines 802-817
"""

import pandas as pd
import os

def load_blood_data(data_path='../Data/blood.txt'):
    """
    Load blood dataset from whitespace-delimited text file
    
    Parameters:
    -----------
    data_path : str
        Path to blood.txt file (relative or absolute)
    
    Returns:
    --------
    pd.DataFrame
        Blood dataset with columns: Subject, Gender, BloodType, AgeGroup, WBC, RBC, Chol
    """
    names = ['Subject', 'Gender', 'BloodType', 'AgeGroup', 'WBC', 'RBC', 'Chol']
    
    blood_df = pd.read_csv(
        data_path,
        sep=r'\s+',  # Any whitespace as delimiter
        names=names,
        na_values='.',  # SAS uses '.' for missing values
        engine='python'  # Needed for regex separator
    )
    
    return blood_df


if __name__ == '__main__':
    df = load_blood_data()
    print(f"Loaded {len(df)} rows")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFirst 10 rows:")
    print(df.head(10))
    print(f"\nData types:")
    print(df.dtypes)
    print(f"\nMissing value counts:")
    print(df.isnull().sum())
