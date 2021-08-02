# Importing necesssary libraries
import matplotlib.pyplot as plt
import random

# Defining values
pokemon = [ 'Water', 'Normal', 'Flying', 'Grass', 'Psychic', 'Bug', 'Fire',
            'Poison', 'Ground', 'Rock', 'Fighting', 'Dark', 'Steel',
            'Electric', 'Dragon', 'Fairy', 'Ghost', 'Ice' ]
power = [ 133, 109, 101, 98, 85, 77, 68, 66, 65, 60, 57, 54, 53, 51, 50,
          50, 46, 40 ]

# Randomly generating RGB color codes for each pie
colors = list()
for i in range(len(pokemon)):
    rgb = (random.uniform(0, .5), random.uniform(0, .5), random.uniform(0, .5))
    colors.append(rgb)

# Exploding the 1st slice of pie
explode = [0] * 18
explode[0] = 0.2

# Adding Theme to graph
plt.style.use('default')

# Setting text size
plt.rcParams['font.size'] = 9.0

# PLotting graph
plt.pie(power, colors=colors, explode=explode,
         startangle=150, autopct='%1.1f%%', textprops=dict(color='white'),
         shadow=True)

# Adding labels to graph
plt.title('Pokemon')

# Adding legend to graph
plt.legend(title='Types', labels=pokemon, loc='right', bbox_to_anchor=(1, 0, 0.2, 1))

# Adjust some padding to graph
plt.tight_layout()

# Showing graph as output
plt.show()
