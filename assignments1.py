import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, num_steps):

    x_values = [x0]
    y_values = [y0]

    for _ in range(num_steps):
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)

    return np.array(x_values), np.array(y_values)

def f(x, y):
    return y - x


x0 = 0
y0 = 1


h = 0.1
num_steps = 100

# Solve using Euler's method
x_values, y_values = euler_method(f, x0, y0, h, num_steps)


plt.plot(x_values, y_values, label="Euler's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of dy/dx = y - x using Euler\'s Method')
plt.legend()
plt.grid(True)
plt.show()
