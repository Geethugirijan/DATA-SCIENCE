import pandas as pd

# Sample dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

print(df)
