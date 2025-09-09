import pandas as pd

# DataFrame 1: Employee details
df1 = pd.DataFrame({
    'EID': [101, 102, 103],
    'ENAME': ['Alice', 'Bob', 'Charlie'],
    'stipend': [5000, 6000, 5500]
})

# DataFrame 2: Employee designation
df2 = pd.DataFrame({
    'EID': [101, 102, 103],
    'designation': ['Manager', 'Developer', 'Analyst']
})

# Merge the two DataFrames on 'EID'
result = pd.merge(df1, df2, on='EID')
print("\nfirst dataframe:\n",df1)
print("\nsecond dataframe:\n",df2)
print("\nresult:\n",result)
