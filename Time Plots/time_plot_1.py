# Importing necesssary libraries
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np

# Defining values
dates = [ datetime(2021,7,29), datetime(2021,7,30), datetime(2021,7,31), datetime(2021,8,1),
            datetime(2021,8,2), datetime(2021,8,3), datetime(2021,8,4) ]
values = list(np.random.randint(low = 0,high=100,size=7))
date_fmt = mpl_dates.DateFormatter('%b, %d %Y')

# PLotiing graph
plt.plot_date(dates, values, linestyle='solid')

# Setting Y axis limits
plt.ylim((0,100))

# Setting figure and axis
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(date_fmt)

# Adjust some padding to graph
plt.tight_layout()

#Saving graph as png
plt.savefig('time_plot_1.png', dpi=300)

# Showing graph as output
plt.show()
