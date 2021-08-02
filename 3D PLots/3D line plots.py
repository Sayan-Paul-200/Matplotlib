# Importing necesssary libraries
import matplotlib.pyplot as plt
import numpy as np
# Defining values

z = np.linspace(0, 30, 200)
x = np.sin(z)
y = np.cos(z)

# PLotting graph
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z)

# Adding labels to graph
ax.set_xlabel(r'$\sin(Z)$', rotation=0)
ax.set_ylabel(r'$\cos(Z)$', rotation=0)
ax.set_zlabel('$Z$', rotation=0)
ax.set_title('My First 3D Plot')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('3D line plot.png', dpi=300)

# Showing graph as output
plt.show()
