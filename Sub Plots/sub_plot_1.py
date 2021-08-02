# Importing necesssary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Assigning values
data = pd.read_csv('subplot_data.csv')
ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']

# Adding style to graph
plt.style.use('ggplot')

# Plotting graphs
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(ages, dev_sal, label='All Developers', linestyle='--', color='#444444')
ax2.plot(ages, py_sal, label='Python')
ax2.plot(ages, js_sal, label='JavaScript')

# Adding labels to graph
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

# Adding legends to graph
ax1.legend()
ax2.legend()

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('sub_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
