import matplotlib.pyplot as plt
import numpy as np

def plot_funtion():

    x = np.linspace(-10,10, 30)
    y = np.arctan(x)

    plt.figure(figsize =(10,6))
    plt.plot(x,y, color = "blue", label="$f(x) = arctg(x)", linestyle = 'dotted', marker = '1')

    plt.legend()
    plt.title('Graph of the Function $f(x) = arctg(x)')
    plt.xlabel('x-axis')
    plt.ylabel('f(x)')
    plt.grid(True)

    plt.show()

plot_funtion()