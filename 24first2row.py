import pandas as pd

# Example DataFrame
data = {
    'A': [2, 1, 2, 1],
    'B': [1, 2, 3, 4],
    'C': [3, 4, 1, 2]
}
df = pd.DataFrame(data)

first_two_rows = df.head(2)

print(first_two_rows)
