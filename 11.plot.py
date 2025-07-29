
import matplotlib.pyplot as plt

# Coordinates
x = [1, 2, 6, 18]
y = [3, 10, 12, 20]

# Plot with red dotted line and green markers
plt.plot(x, y, color='red', linestyle=':', marker='o',
         markerfacecolor='green', markeredgecolor='green', markersize=10)

# Add labels to each point
for i in range(len(x)):
    plt.text(x[i] + 0.2, y[i], f"({x[i]}, {y[i]})", fontsize=9)

# Labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('GRAPH')
plt.grid(True)

# Save the plot to an image file
plt.savefig("line_plot.png")

# If in an environment with GUI backend, you could also call plt.show()
# plt.show()
