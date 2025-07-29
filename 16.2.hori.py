import matplotlib.pyplot as plt
languages=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.barh(languages,popularity,color='plum')
plt.title('programming languages popularity')
plt.xlabel('popularity')
plt.ylabel('languages')
plt.grid(True,axis='x')
plt.savefig('graph7')
