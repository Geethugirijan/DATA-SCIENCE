import pandas as pd

# Generate date range from 1st May 2021 to 12th May 2021
date_series = pd.date_range(start='2021-05-01', end='2021-05-12')
date_series =pd.Series(date_series)
# Display the date series
print("Date Series from 1st May 2021 to 12th May 2021:")
print(date_series)
