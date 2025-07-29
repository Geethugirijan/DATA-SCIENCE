import matplotlib.pyplot as plt
x = [0, 1, 2, 3]
y = [3, 8, 1, 10]

plt.subplot(2, 3, 1)
plt.plot(x,y)

x =[0, 1, 2, 3]
y =[10, 20, 30, 40]

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = [0, 1, 2, 3]
y = [3, 5, 1, 19]

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = [0, 1, 2, 3]
y = [19, 12, 3, 20]

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = [0, 1, 2, 3]
y = [2, 18, 1, 12]

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = [0, 1, 2, 3]
y = [11, 22, 3, 14]

plt.subplot(2, 3, 6)
plt.plot(x,y)

#plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig('graph5.png')

