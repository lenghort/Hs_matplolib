import numpy as np
import matplotlib.pyplot as plt

def plot_function():
    x = np. linspace(-3,3,30)
    y = np. linspace(-3,3,30)
    X,Y = np.meshgrid(x,y)

    Z = X**2 + Y**2

    fig= plt.figure(figsize =(10,6))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
    fig.colorbar(surf, ax=ax, label='f(x, y) = x**2 + y**2')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title('Surface Plot of f(x, y) = x**2 + y**2')

    plt.show()

plot_function()