import matplotlib.pyplot as plt
import numpy as np

points = np.loadtxt('points.csv', delimiter=',')
distances = np.loadtxt('distances.csv', delimiter = ',')

x = points[:, 0] 
y = points[:, 1]  

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=distances, cmap='viridis') 

plt.colorbar(scatter, label='Distance')

plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Scatter Plot of Points Colored by Distance')
plt.grid(True)

plt.show()