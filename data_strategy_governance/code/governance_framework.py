# governance_framework.py

import pandas as pd

def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data > 0]
    return pd.DataFrame({'Column': missing_data.index, 'Missing Count': missing_data.values})

def enforce_column_naming_conventions(df: pd.DataFrame, pattern: str = '^[a-z_]+$') -> None:
    import re
    invalid_columns = [col for col in df.columns if not re.match(pattern, col)]
    if invalid_columns:
        raise ValueError(f"Columns {invalid_columns} do not follow the naming convention pattern: {pattern}")

if __name__ == "__main__":
    data = {
        'customer_id': [1, 2, 3, None],
        'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, None, 35, 45]
    }

    df = pd.DataFrame(data)

    print("Checking for missing values...")
    print(check_missing_values(df))

    try:
        print("\nEnforcing column naming conventions...")
        enforce_column_naming_conventions(df)
    except ValueError as e:
        print(f"Governance issue: {e}")
