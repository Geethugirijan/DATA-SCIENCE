import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(8, 8))  # Optional: makes the pie chart look better
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Programming Languages Popularity')
plt.axis('equal')
plt.savefig('graph10.png')

