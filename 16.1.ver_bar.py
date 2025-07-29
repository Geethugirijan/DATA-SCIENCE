import matplotlib.pyplot as plt
languages=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(languages,popularity,color='plum',width=0.4)
plt.title('programming languages popularity')
plt.xlabel('languages')
plt.ylabel('popularity')
plt.grid(True,axis='y')
plt.savefig('graph6')
