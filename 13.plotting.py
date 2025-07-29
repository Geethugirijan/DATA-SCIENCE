import matplotlib.pyplot as plt
x=[]
y=[]
with open('test.txt','r') as file:
    for line in file:
        parts=line.strip().split()
        if len(parts)==2:
            x.append(float(parts[0]))
            y.append(float(parts[1]))
plt.plot(x,y,marker='o',linestyle='-',color='green')
plt.title('LINE PLOT FROM FILE DATA')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.savefig("graph3.png")
#plt.show()