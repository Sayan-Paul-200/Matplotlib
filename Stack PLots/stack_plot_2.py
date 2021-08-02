# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
hours = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
dev_1 = [ 8, 6, 5, 5, 4, 2, 1, 1, 0 ]
dev_2 = [ 0, 1, 2, 2, 2, 4, 4, 4, 4 ]
dev_3 = [ 0, 1, 1, 1, 2, 2, 3, 3, 4 ]
labels = [ 'Dev 1', 'Dev 2', 'Dev 3' ]
colors = [ '#6d904f', '#fc4f30', '#008fd5' ]

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.stackplot(hours, dev_1, dev_2, dev_3, colors=colors, labels=labels)

# Adding labels to graph
plt.title('Developers Work Distribution')
plt.ylabel('Work Rates')
plt.xlabel('Hours')

# Adding legend to graph
plt.legend(title='Developers', loc=(1.01, 0.8))

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('stack_plot_2.png', dpi=300)

# Showing graph as output
plt.show()
