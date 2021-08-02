# Importing necesssary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Defining values
data = pd.read_csv('lineplot_data.csv')
ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']
ovr_median = 57287

# Adding Theme to graph
plt.style.use('default')

# PLotting graph
plt.plot(ages, py_sal, label='Python Developers')
plt.plot(ages, js_sal, label='JavaScript Developers')
plt.plot(ages, dev_sal, color='#444444', linestyle='--', label='All Developers')

# Fill between plots
plt.fill_between(ages, py_sal, dev_sal, where=(py_sal>dev_sal),
                  interpolate=True, alpha=0.25, label='Above Median')
plt.fill_between(ages, py_sal, dev_sal, where=(py_sal<=dev_sal),
                  interpolate=True, color='red', alpha=0.25,
                  label='Below Median')

# Adding labels to graph
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

# Adding legend to graph
plt.legend(title='Legend')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('line_plot.png', dpi=300)

# Showing graph as output
plt.show()
