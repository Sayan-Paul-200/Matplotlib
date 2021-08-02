# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
ages = [ 18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55 ]
bins = [ 10, 20, 30, 40, 50, 60 ]

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.hist(ages, bins=bins, edgecolor='black')

# Adding labels to graph
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.title('Ages of Respondents')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('hist_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
