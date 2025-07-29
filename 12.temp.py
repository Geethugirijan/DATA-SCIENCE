import matplotlib.pyplot as plt
temperature=[12,14,16,18,20,22,24]
sales=[100,200,250,400,300,450,500]
plt.plot(temperature,sales,marker='o',linestyle='-',color='green')
plt.title('TEMPERATURE VS SALES')
plt.xlabel('TEMPERATURE')
plt.ylabel('SALES')
plt.grid(True)
plt.savefig("graph2.png")
#plt.show()