# Importing necesssary libraries
import matplotlib.pyplot as plt
import numpy as np

# Defining values
ages_x = [ 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 ]
dev_y = [ 38496, 42000, 46752, 49320, 53200, 56000,
          62316, 64928, 67317, 68748, 73572 ]
py_dev_y = [ 45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640 ]
js_dev_y = [ 37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583 ]
x_indices = np.arange(len(ages_x))
width = 0.25

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.bar(x_indices - width, py_dev_y, width=width, label='Python Developers')
plt.bar(x_indices, js_dev_y, width=width, label='JS Developers')
plt.bar(x_indices + width, dev_y, width=width, label='All Developers')

# Adding labels to graph
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.xticks(x_indices, labels=ages_x)

# Adding grid to graph
plt.grid(True)

# Adjust some padding to graph
plt.tight_layout()

# Adding legend to graph
plt.legend(title='Legend')

 # Saving graph as png
plt.savefig('bar_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
