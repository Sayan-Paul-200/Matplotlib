# Importing necesssary libraries
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np

# Defining values
data = pd.read_csv('timeplot_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
dates = data['Date']
price_close = data['Close']

# PLotting graph
plt.plot_date(dates, price_close, linestyle='solid')

# Setting date format
date_fmt = mpl_dates.DateFormatter('%b, %d %Y')
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(date_fmt)

# Adding labels to graph
plt.ylabel('Closing Price (USD)')
plt.title('Closing Price Trends')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('time_plot_2.png', dpi=300)

# Showing graph as output
plt.show()
