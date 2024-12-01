import numpy as np
import matplotlib.pyplot as plt

# Define the regions for the events
x = np.linspace(0, 3, 300)
y = np.linspace(0, 2, 200)
X, Y = np.meshgrid(x, y)

# Event: Both calls within the first hour
plt.figure(figsize=(10, 6))
plt.fill_between([0, 1], 0, 1, color='blue', alpha=0.3, label='Both calls within the first hour')
plt.fill_between([1, 3], 1, 2, color='red', alpha=0.3, label='Neither call within the first hour')
plt.plot([0, 3], [0, 2], color='green', label='X calls before Y')

plt.xlim(0, 3)
plt.ylim(0, 2)
plt.xlabel('X (hours)')
plt.ylabel('Y (hours)')
plt.title('Events in the X-Y Plane')
plt.legend()
plt.grid(True)
plt.show()