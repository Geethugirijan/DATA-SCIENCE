import pandas as pd

# Sample 2D list
data = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 35]
]

# Convert 2D list to DataFrame with custom column names
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

print(df)
