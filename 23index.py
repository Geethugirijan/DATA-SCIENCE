import pandas as pd

# Example DataFrame with a custom index
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]
}, index=['x', 'y', 'z'])

print("Original DataFrame:")
print(df)
# Reset index to default integer index
df_reset = df.reset_index(drop=True)

print("\nDataFrame with default integer index:")
print(df_reset)