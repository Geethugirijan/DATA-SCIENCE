import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,4,9,16,25]
p=[1,2,3,4,5]
q=[2,3,5,7,11]
plt.plot(x,y,label='square',marker='o',color='green')
plt.plot(x,p,label='linear',linestyle='--',color='blue')
plt.plot(x,q,label='prime',linestyle='-.',color='red')
plt.title('multiple lines')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True)
plt.savefig("graph4.png")
#plt.show()

