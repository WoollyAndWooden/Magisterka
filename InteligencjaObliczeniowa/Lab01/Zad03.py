import pandas as pd
from difflib import SequenceMatcher

df = pd.read_csv("iris_with_errors.csv")

df[df.columns[0:4]] = df[df.columns[0:4]].apply(pd.to_numeric, errors="coerce").round(1)

incomplete_rows = df.isnull().any(axis=1).sum()

print(incomplete_rows)

numeric_cols = df.select_dtypes(include="number").columns

print(df.values[34, :])

for col in numeric_cols:
    median_val = df[col].median()
    invalid_mask = (df[col] <= 0) | (df[col] >= 15) | (df[col].isnull())
    df.loc[invalid_mask, col] = median_val

print(df.values[34, :])

iris_names = ["Setosa", "Versicolor", "Virginica"]

names_mask = ~df[df.columns[4]].isin(iris_names)

for i, val in zip(df.index[names_mask], df[df.columns[4]][names_mask]):
    print(f"Row {i}, value: {val}")
    check = {y: SequenceMatcher(None, str(val), y).ratio() for y in iris_names}
    correct = max(check, key=check.get)
    df.at[i, df.columns[4]] = correct
    print(f"Now value = {df.values[i, 4]}")