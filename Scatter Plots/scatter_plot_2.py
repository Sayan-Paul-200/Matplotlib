# Importing necesssary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Defining values
data = pd.read_csv('scatterplot_data.csv')
views = data['view_count']
likes = data['likes']
ratio = data['ratio']

# Adding Theme to graph
plt.style.use('seaborn')

# PLotting graph
plt.scatter(views, likes, c=ratio, cmap='summer',
            edgecolor='black', linewidth=1, alpha=0.75)
plt.xscale('log')
plt.yscale('log')

# Setting Colour map
cbar = plt.colorbar()
cbar.set_label('Like - Dislike Ratio')

# Adding labels to graph
plt.xlabel('View Counts')
plt.ylabel('Total Likes')
plt.title('Youtube - Top Trending Videos - 2019')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('scatter_plot_2.png', dpi=300)

# Showing graph as output
plt.show()
