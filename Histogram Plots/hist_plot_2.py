# Importing necesssary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Defining values
data = pd.read_csv('histplot_data.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
median_age = int(data['Age'].median())

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# PLotting graph
plt.hist(ages, bins=bins, edgecolor='black', log=True)
plt.axvline(median_age, color='#fc4f30', linewidth=2, label='Median Age')

# Adding labels to graph
plt.xlabel('Ages')
plt.ylabel('Total Respondents (log scale)')
plt.title('Ages of Respondents')

# Adding legend to graph
plt.legend()

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('hist_plot_2.png', dpi=300)

# Showing graph as output
plt.show()
