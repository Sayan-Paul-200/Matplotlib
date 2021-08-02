# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
slices = [ 60, 40, 30, 20 ]
labels = [ 'Sixty', 'Forty', 'Thirty', 'Twenty' ]
colors = [ '#008fd5', '#fc4f30', '#e5ae37', '#6d904f' ]

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'})

# Adding labels to graph
plt.title('My Awesome Pie-Chart')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('pie_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
