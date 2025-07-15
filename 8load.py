import numpy as np
my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
filename = 'my_data.txt'
np.savetxt(filename, my_array)
print("Array saved to", filename)
