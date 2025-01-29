
import matplotlib.pyplot as plt
import numpy as np

def plot_funtion():
    x = np.linspace(-10,10, 30)
    y = x**2

    plt.figure(figsize =(10,6))
    plt.plot(x,y, color = "green", label="$f(x) = x^2$", marker = '1')

    plt.legend()
    plt.title('Graph of the Function $f(x) = x^2$')
    plt.xlabel('x-axis')
    plt.ylabel('f(x)')
    plt.grid(True)

    plt.show()

plot_funtion()
