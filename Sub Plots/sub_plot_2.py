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

# Assigning subplots variables
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# Plotting graphs
ax1.plot(ages, dev_sal, label='All Developers', linestyle='--', color='#444444')
ax2.plot(ages, py_sal, label='Python')
ax2.plot(ages, js_sal, label='JavaScript')

# Setting labels for subplots
ax1.set_title('All Developers Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.set_title('Python - JavaScript Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

# Setting legends
ax1.legend()
ax2.legend()

# Adjust some padding to graph
plt.tight_layout()

# Saving suplots as separate png files
fig1.savefig('Subplot Figure 1.png')
fig2.savefig('Subplot Figure 2.png')

# Showing graph as output
plt.show()
