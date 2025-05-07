import pandas as pd

def clean_dataframe(df):
    df = df.copy()  # avoid modifying original

    # Fill numeric columns with median
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        median = df[col].median()
        df[col].fillna(median, inplace=True)

    # Fill non-numeric columns with mode
    non_num_cols = df.select_dtypes(exclude='number').columns
    for col in non_num_cols:
        if df[col].isnull().any():
            mode = df[col].mode(dropna=True)
            if not mode.empty:
                df[col].fillna(mode[0], inplace=True)

    return df
