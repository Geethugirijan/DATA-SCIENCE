import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Occupation': ['Engineer', 'Doctor', 'Engineer', 'Doctor', 'Artist'],
    'Salary': [70000, 120000, 80000, 110000, 50000]
}

df = pd.DataFrame(data)

avg_salary = df.groupby('Occupation')['Salary'].mean()
print(avg_salary)
