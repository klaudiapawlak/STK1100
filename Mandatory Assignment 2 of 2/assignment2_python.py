import numpy as np
import matplotlib.pyplot as plt

# Constant values for the minimum income (k) and the shape parameter (t)
k = 400000
t = 3

# Inverse transformation function to generate values from the distribution
def F_invers(x):
    return k / (1 - x)**(1/t)

# Probability density function (PDF) of the Pareto distribution
def f(x):
    return t * k**t * x**(-t - 1)

# Number of samples to simulate
n = 10000

# Generate n random numbers from a uniform distribution on [0, 1)
u = np.random.uniform(0, 1, n)

# Apply inverse transform sampling to get income values
p = F_invers(u)

# Print the median and mean of the simulated incomes
print("median = %f" % (np.median(p)))
print("mean = %f" % (np.mean(p)))

# Create x-values from the minimum income up to 2 million for plotting the PDF
x = np.linspace(k, 2000000, n)

# Calculate the theoretical density values for plotting
density = f(x)

# Plot histogram of the simulated income data
plt.xlim(300000, 2000000)
plt.hist(p, density=True, edgecolor="black", bins=300)

# Plot the theoretical density curve
plt.plot(x, density)

# Set axis labels
plt.xlabel("Annual Income")
plt.ylabel("Probability")
plt.show()
