# Importing necesssary libraries
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter

# Defining values
with open('barplot_data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lang_counter = Counter()
    for row in csv_reader:
        lang_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = list()
popularity = list()
for item in lang_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

# Adding Theme to graph
plt.style.use('seaborn')

# PLotting graph
plt.barh(languages, popularity)

# Adding labels to graph
plt.xlabel('Number of people used')
plt.title('Most Popular Languages')

# Adjust some padding to graph
plt.tight_layout()

 # Saving graph as png
plt.savefig('bar_plot_2.png', dpi=300)

# Showing graph as output
plt.show()
