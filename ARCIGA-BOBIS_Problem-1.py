# Import_libraries
import matplotlib.pyplot as plt
import numpy as np

# Set n to 0:199
x = np.arange(0, 100).tolist()
# Set an array of length 200 to be modified later
y = np.zeros(100)

# Applying the given piecewise-defined function
for k in range(0, 100):
    # Uses the first condition in the function
    if k <= 9: 
        y[k] = x[k] ** 2 - 7
   # Uses the second condition in the function
    else: 
        y[k] = y[k-10]

# Plotting the function using stem()
plt.stem(x, y, use_line_collection=True)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis f(n)')
plt.title('Plot of the Piecewise-Defined Function')
plt.show()

# Observation: The plot is periodic