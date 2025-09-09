import pandas as pd

# Sample list
my_list = [10, 20, 30, 40, 50]

# Convert list to Series
my_series = pd.Series(my_list)

# Display the Series
print("Original List:", my_list)
print("\nConverted Pandas Series:")
print(my_series)
