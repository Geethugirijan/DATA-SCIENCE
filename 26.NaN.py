import pandas as pd
import numpy as np

# Sample DataFrame with NaN values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 5, 6, np.nan]
}
df = pd.DataFrame(data)

# Fill NaN values with zero
df_filled = df.fillna(0)

print(df_filled)
