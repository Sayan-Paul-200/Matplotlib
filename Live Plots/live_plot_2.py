# Importing necesssary libraries
import pandas as pd
import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

# Defining values
index = count()

# Defining plot style
plt.style.use('fivethirtyeight')

# Defining function for animation
#x = list()
#y = list()
def animate(i):
    data = pd.read_csv('liveplot_data.csv')
    x = data['x_val']
    y1 = data['total_1']
    y2 = data['total_2']
    plt.cla()
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.title('Live Subscriber Count')
    plt.xlabel('Hours')
    plt.ylabel('Subscribers')
    plt.legend(loc='upper left')
    plt.tight_layout()

# Plotting graph
animation = FuncAnimation(plt.gcf(), animate, interval=1000)

# Adjust some padding to graph
plt.tight_layout()

# Showing graph as output
plt.show()
