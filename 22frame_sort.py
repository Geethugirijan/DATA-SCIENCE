
import pandas as pd

# Example DataFrame
data = {
    'A': [2, 1, 2, 1],
    'B': [1, 2, 3, 4],
    'C': [3, 4, 1, 2]
}
df = pd.DataFrame(data)
print("Before sorting:\n",df)

# Sort by column 'A' ascending, then by column 'B' descending
df_sorted = df.sort_values(by=['A', 'B'], ascending=[True, False])

print("After sorting:\n",df_sorted)
