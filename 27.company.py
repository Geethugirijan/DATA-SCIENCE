import pandas as pd

# Sample data
data = {
    'cname': ['Company A', 'Company B', 'Company C', 'Company D'],
    'profit': [1000, -500, 0, 200]
}

df = pd.DataFrame(data)

# Convert profit values: profit > 0 -> True, else False
df['profit'] = df['profit'] > 0

print(df)
