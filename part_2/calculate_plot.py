import numpy as np
import matplotlib.pyplot as plt

numbers = np.loadtxt('values_for_bars.csv', delimiter = ',', dtype=int)
values, frequencies = np.unique(numbers, return_counts=True)

plt.bar(values, frequencies, color='orange')
plt.xlabel("Numbers")
plt.ylabel("Frequencies")
plt.title("Number Frequencies with NumPy")
plt.legend()
plt.show()