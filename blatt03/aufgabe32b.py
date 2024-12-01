import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
n = 10  # Number of discrete points
mu = 0  # Mean of the normal distribution
sigma = 1  # Standard deviation of the normal distribution

# Generate discrete values for X
i_values = np.arange(1, n + 1)  # Array of values from 1 to n
p_i = (i_values - 0.5) / n  # Probabilities for the discrete points
z_pi = norm.ppf(p_i)  # Inverse CDF (percent point function) to get z-scores

# Discrete CDF values for X
X_values = z_pi  # Discrete z-scores
F_X_values = np.cumsum([1 / n] * n)  # Cumulative sum to get CDF values

# Generate continuous values for Y
y_values = np.linspace(-3, 3, 500)  # Array of 500 evenly spaced values between -3 and 3
F_Y_values = norm.cdf(y_values, loc=mu, scale=sigma)  # CDF values for the normal distribution

# Plotting the CDFs
plt.figure(figsize=(10, 6))  # Create a figure with a specific size
plt.step(X_values, F_X_values, label="$F^X(x)$", where='post', color="blue")  # Step plot for the discrete CDF
plt.plot(y_values, F_Y_values, label="$F^Y(y)$", color="green")  # Line plot for the continuous CDF
plt.title("Verteilungsfunktionen von $X$ und $Y$")  # Title of the plot
plt.xlabel("$x, y$")  # Label for the x-axis
plt.ylabel("Wahrscheinlichkeit")  # Label for the y-axis
plt.grid(True)  # Enable grid
plt.legend()  # Show legend
plt.show()  # Display the plot