# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
ages_x = [ 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 ]
dev_y = [ 38496, 42000, 46752, 49320, 53200, 56000,
          62316, 64928, 67317, 68748, 73572 ]
py_dev_y = [ 45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640 ]
js_dev_y = [ 37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583 ]

# Adding Theme to graph
# To see all themes avalibale ----> print(plt.style.available)
plt.style.use('seaborn')
# To use a theme like the XKCD Comics, ----> plt.xkcd()

# PLotting graph
plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python Developers')
plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JS Developers')
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Developers')

# Adding labels to graph
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

# Adding grid to graph
plt.grid(True)

# Saving graph as file
plt.savefig('plot_1.png', dpi=300)

# Adding legend to graph
plt.legend(title='Legend')

# Adjust some padding to graph
plt.tight_layout()

# Showing graph as output
plt.show()
