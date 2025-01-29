import numpy as np
import matplotlib.pyplot as plt

def plot_funtion():
    x = np.linspace(-3, 3, 30)
    y = np.linspace(-3, 3, 30)
    X,Y = np.meshgrid(x,y)

    Z = X * Y
    
    fig= plt.figure(figsize =(10,6))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
    fig.colorbar(surf, ax=ax, label='f(x, y) = x * y')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title('Surface Plot of f(x, y) = x * y')

    plt.show()

plot_funtion()