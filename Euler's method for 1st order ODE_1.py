import matplotlib.pyplot as plt
import numpy as np

# Define initial conditions and parameters
x_0 = 0  # Initial x value
y_0 = 1  # Initial y value
Δx = 0.5  # Step size
N = 10  # Number of steps

# Function defining the derivative dy/dx = (y^2 - x^2) / 5
def f(x, y):
    return (y**2 - x**2) / 5 #This is 1st-order ODE

# Arrays for storing x and y values
x_list = [x_0]
y_list = [y_0]

# Euler's method
x = x_0
y = y_0

for _ in range(N):
    y = y + Δx * f(x, y)  # Update y using Euler's formula
    x = x + Δx  # Increment x
    x_list.append(x)
    y_list.append(y)

# Convert lists to arrays for plotting
x_plot = np.array(x_list)
y_plot = np.array(y_list)

# Plot the results
plt.scatter(x_plot, y_plot, color='red', label='Euler Approximation')
plt.plot(x_plot, y_plot, color='blue', linestyle='dashed')  # Add a line for better visualization
plt.title("Euler's Method Approximation")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
