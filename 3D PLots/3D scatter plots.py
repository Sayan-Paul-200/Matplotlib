# Importing necesssary libraries
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# Setting mean, standard deviation and sample size
mean = 10
std_deviation = 1
n = 500

# Creating 3 random sets of normally (Gaussian) distributed data
x = np.random.normal(mean, std_deviation, n)
y = np.random.normal(mean, std_deviation, n)
z = np.random.normal(mean, std_deviation, n)

# PLotting graph
fig = plt.figure(figsize=(6,4.5))
ax = plt.axes(projection='3d')
scatter_plot = ax.scatter3D(x, y, z, s=(x+y+z)*1.5, alpha=0.5, c=(x+y+z), cmap='cool', marker='o')

# Setting Colour Bar
min_list = [ x.min(), y.min(), z.min() ]
min_val = int(min(min_list))
max_list = [ x.max(), y.max(), z.max() ]
max_val = int(max(max_list))
cbar_ticks = np.arange(min_val, max_val+1, 1)
cbar = plt.colorbar(scatter_plot, pad=0.05, shrink=0.8, aspect=15)

# Adjust some padding to graph
plt.tight_layout()

# Showing graph as output
plt.show()

print(min_val, max_val, cbar_ticks)
