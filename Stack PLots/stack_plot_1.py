# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player_2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player_3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.stackplot(minutes, player_1, player_2, player_3,)

# Adding labels to graph
plt.title('My Awesome Stack Plot')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('stack_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
