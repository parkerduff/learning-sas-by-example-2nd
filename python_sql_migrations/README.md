# Python & SQL Migration of SAS Blood Dataset Examples

This directory contains Python and SQL implementations equivalent to the SAS code examples that work with the blood dataset from `Data/blood.txt`.

## Overview

The migration follows the test-driven approach outlined in the migration plan document. Each SAS procedure has been converted to equivalent Python (using pandas) and SQL implementations.

## Files

### Data Loading
- **`load_blood_data.py`** - Loads `blood.txt` into pandas DataFrame
  - Equivalent to SAS DATA step from `Create_Datasets.sas` lines 802-817
  - Handles whitespace-delimited format and missing value conversion

### Python Procedure Migrations

- **`proc_means_migration.py`** - Statistical summary using pandas
  - Uses `df.agg()` with statistics (N, NMISS, Mean, Median, Min, Max)
  - Equivalent to `Programs Used in the Second Edition.sas` lines 2176-2185

- **`proc_report_migration.py`** - Cross-tabulation report using pandas
  - Uses `pivot_table()` for multi-dimensional analysis
  - Equivalent to `Programs Used in the Second Edition.sas` lines 2163-2171

- **`proc_tabulate_migration.py`** - Table layouts using pandas (multiple examples)
  - Uses `crosstab()` and `pivot_table()` with margins
  - Equivalent to `Programs Used in the Second Edition.sas` lines 2492-2534
  - Includes examples 18-4, 18-5, 18-8, and 18-9

- **`proc_sql_migration.py`** - Calculated percentages using pandas
  - Calculates mean and percentages on first 10 observations
  - Equivalent to `Solutions_to_Odd_Numbered_problems.sas` lines 1901-1915

### SQL Queries (Standalone Files)

- **`create_table.sql`** - Table schema and data loading examples
- **`proc_means.sql`** - Statistical summary using SQL aggregates
- **`proc_report.sql`** - Cross-tabulation using CASE statements and GROUP BY
- **`proc_tabulate.sql`** - Multiple table layouts using CASE statements and ROLLUP
- **`proc_sql.sql`** - Calculated percentages using CTEs (Common Table Expressions)

## Prerequisites

### Python Environment
```bash
pip install pandas
```

Or using conda:
```bash
conda install pandas
```

### Tested Versions
- Python 3.8+
- pandas >= 1.3.0

## Usage

### Running Individual Migrations

Each migration script can be run standalone to see the Python output and SQL equivalent:

```bash
# From the python_sql_migrations directory
python load_blood_data.py
python proc_means_migration.py
python proc_report_migration.py
python proc_tabulate_migration.py
python proc_sql_migration.py
```

### Using as Python Modules

You can also import and use the functions in your own scripts:

```python
from load_blood_data import load_blood_data
from proc_means_migration import proc_means

# Load the blood dataset
df = load_blood_data()

# Calculate statistics
stats = proc_means(df, variables=['RBC', 'WBC'], maxdec=1)
print(stats)
```

### SQL Execution

The SQL queries are provided as standalone `.sql` files that can be executed in any SQL database after loading the blood dataset.

**Setup Steps:**

1. **Create the table and load data** using `create_table.sql`
2. **Run any of the procedure SQL files:**
   - `proc_means.sql` - Statistical summaries
   - `proc_report.sql` - Cross-tabulation reports
   - `proc_tabulate.sql` - Various table layouts
   - `proc_sql.sql` - Percentage calculations

**PostgreSQL Example:**
```bash
# Create table and load data
psql -d your_database -f create_table.sql

# Then manually load the data or use COPY command
psql -d your_database -c "COPY blood FROM '/path/to/Data/blood.txt' WITH (FORMAT text, DELIMITER E'\t', NULL '.');"

# Run any procedure query
psql -d your_database -f proc_means.sql
psql -d your_database -f proc_report.sql
```

**MySQL Example:**
```bash
# Create table
mysql -u username -p database_name < create_table.sql

# Run procedure queries
mysql -u username -p database_name < proc_means.sql
```

## Output Examples

### PROC MEANS Migration
```
Variable    N  N_Miss  Mean  Median   Min    Max
     RBC  959      42   5.7     5.6   2.6   8.8
     WBC  967      34   6.9     6.7   4.1  10.3
```

### PROC REPORT Migration
```
  Gender BloodType  Old_WBC  Young_WBC  Old_RBC  Young_RBC
  Female         A   6845.0     7248.0     5.50       5.52
  Female        AB   7703.0     7173.0     5.33       5.23
  Female         B   6873.0     6720.0     5.44       5.02
  Female         O   6819.0     6989.0     5.46       5.58
    Male         A   6907.0     7076.0     5.49       5.62
    Male        AB   7170.0     7820.0     5.84       5.45
    Male         B   6616.0     6247.0     5.61       5.62
    Male         O   6790.0     6879.0     5.48       5.60
```

### PROC TABULATE Migration (Example 18-9)
```
         Old                      Young                     All
         RBC    WBC    Chol       RBC    WBC    Chol      RBC    WBC    Chol
Gender                                                                      
Female  5.47  6847.0  195.2      5.54  7125.0  206.5     5.51  6988.0  201.0
Male    5.52  6854.0  193.5      5.61  6995.0  205.1     5.57  6926.0  199.5
All     5.50  6850.0  194.3      5.58  7055.0  205.8     5.54  6956.0  200.2
```

### PROC SQL Migration
```
Subject   RBC   WBC  MeanRBC  MeanWBC  Percent_RBC  Percent_WBC
      1  7.40  7710     6.18     7087       119.74        108.79
      2  4.70  6560     6.18     7087        76.05         92.56
      3  7.53  5690     6.18     7087       121.84         80.30
      ...
```

## Migration Details

### Missing Value Handling
- SAS uses '.' for missing numeric values
- Python uses NaN (Not a Number)
- SQL uses NULL
- All implementations exclude missing values from calculations by default

### Decimal Precision
- Output precision matches SAS format specifications
- PROC MEANS: 1 decimal place (maxdec=1)
- PROC REPORT: WBC = 0 decimals, RBC = 2 decimals
- PROC TABULATE: 2 decimals (format=comma9.2 or comma11.2)

### Data Types
- String columns: Gender (6 chars), BloodType (2 chars), AgeGroup (5 chars)
- Numeric columns: Subject (integer), WBC, RBC, Chol (float with up to 2 decimals)

## Testing

To verify the migration outputs match the SAS outputs:

1. Run the SAS code on the original `blood.txt` dataset
2. Save SAS outputs as test fixtures
3. Run the Python implementations
4. Compare outputs using the verification approach in the migration plan

See the main migration plan document for detailed testing procedures.

## Known Differences

### Median Calculation
- SAS uses a specific interpolation method for median
- Python/SQL may use slightly different algorithms
- Differences are typically negligible for large datasets

### Floating Point Precision
- Minor rounding differences may occur (typically < 1e-8)
- This is expected due to different internal representations

## SQL Database Compatibility

The SQL queries use standard SQL syntax but may need slight adjustments for specific databases:

- **PostgreSQL**: Native support for PERCENTILE_CONT and ROLLUP
- **MySQL**: Use different syntax for percentile calculation
- **SQLite**: Limited window function support in older versions
- **SQL Server**: Full support with minimal syntax changes

## License

This code follows the same license as the parent repository.

## References

- Original SAS code: `Example code/` directory
- Data file: `Data/blood.txt`
- Migration plan: See main repository documentation
