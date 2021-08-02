# Importing necesssary libraries
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# Defining function for z
def func_z(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Assigning values for inputs x and y
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

# Converting x and y to matrices
x, y = np.meshgrid(x, y)

# Assigning z
z = func_z(x, y)

# PLotting graph
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='inferno', edgecolor='none')

# Adding labels to graph
ax.set_xlabel('$x$', rotation=0)
ax.set_ylabel('$y$', rotation=0)
ax.set_zlabel(r'$\sin( \sqrt{ x^{2} + y^{2} } )$', rotation=0)
ax.set_title('3D Surface Plot')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('3D surface plot.png', dpi=300)

# Showing graph as output
plt.show()
