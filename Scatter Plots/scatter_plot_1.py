# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
x = [ 5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1 ]
y = [ 7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1 ]
colors = [ 7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5 ]
sizes = [ 209, 486, 381, 255, 191, 315, 185, 228, 174,
          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539 ]

# Adding Theme to graph
plt.style.use('seaborn')

# PLotting graph
plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', marker='X',
            edgecolor='black', linewidth=1, alpha=0.75)

# Setting Colour map
cbar = plt.colorbar()
cbar.set_label('Satisfaction Levels')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('scatter_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
