# Importing necesssary libraries
import matplotlib.pyplot as plt

# Defining values
slices = [59219, 55466, 47544, 36443, 35917 ]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java' ]
explode = [ 0, 0, 0, 0.1, 0 ]

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.pie(slices, labels=labels, explode=explode, startangle=90,
        wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%', shadow=True)

# Adding labels to graph
plt.title('My Awesome Pie-Chart')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('pie_plot_2.png', dpi=300)

# Showing graph as output
plt.show()
