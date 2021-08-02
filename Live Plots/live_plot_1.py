# Importing necesssary libraries
import pandas as pd
import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

# Defining values
index = count()

# Defining function for animation
x = list()
y = list()
def animate(i):
    x.append(next(index))
    y.append(random.randint(0,10))
    plt.cla()
    plt.title('Live Plotting')
    plt.xlabel('Seconds')
    plt.ylabel('Random value')
    plt.plot(x,y)

# Plotting graph
animation = FuncAnimation(plt.gcf(), animate, interval=1000)

# Adjust some padding to graph
plt.tight_layout()

# Showing graph as output
plt.show()
