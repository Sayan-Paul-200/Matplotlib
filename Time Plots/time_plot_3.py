# Importing necesssary libraries
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np

# Facebook Data
fb = pd.read_csv('FB_data.csv')
fb['Date'] = pd.to_datetime(fb['Date'])
fb.sort_values('Date', ascending=False, inplace=True)
fb_dates = fb['Date']
fb_cp = fb['Close']

# Amazon Data
amzn = pd.read_csv('AMZN_data.csv')
amzn['Date'] = pd.to_datetime(amzn['Date'])
amzn.sort_values('Date', ascending=False, inplace=True)
amzn_dates = amzn['Date']
amzn_cp = amzn['Close']

# Apple Data
aapl = pd.read_csv('AAPL_data.csv')
aapl['Date'] = pd.to_datetime(aapl['Date'])
aapl.sort_values('Date', ascending=False, inplace=True)
aapl_dates = aapl['Date']
aapl_cp = aapl['Close']

# Netflix Data
nflx = pd.read_csv('NFLX_data.csv')
nflx['Date'] = pd.to_datetime(nflx['Date'])
nflx.sort_values('Date', ascending=False, inplace=True)
nflx_dates = nflx['Date']
nflx_cp = nflx['Close']

# Google Data
goog = pd.read_csv('GOOG_data.csv')
goog['Date'] = pd.to_datetime(goog['Date'])
goog.sort_values('Date', ascending=False, inplace=True)
goog_dates = goog['Date']
goog_cp = goog['Close']

# Adding Theme to graph
plt.style.use('fivethirtyeight')

# Setting text size
plt.rcParams['font.size'] = 8.0

# PLotting graph
plt.plot_date(fb_dates[::10], fb_cp[::10], linestyle='solid', linewidth=2, markersize=4, label='Facebook')
plt.plot_date(amzn_dates[::10], amzn_cp[::10], linestyle='solid', linewidth=2, markersize=4, label='Amazon')
plt.plot_date(aapl_dates[::10], aapl_cp[::10], linestyle='solid', linewidth=2, markersize=4, label='Apple')
plt.plot_date(nflx_dates[::10], nflx_cp[::10], linestyle='solid', linewidth=2, markersize=4, label='Netflix')
plt.plot_date(goog_dates[::10], goog_cp[::10], linestyle='solid', linewidth=2, markersize=4, label='Google')

# Setting date ticks and limits
start_date = fb_dates.iloc[0]
all_days_within_a_year = [start_date - timedelta(days=x) for x in range(366)]

first_days_of_month = list()
for i, d in enumerate(all_days_within_a_year):
    if d.day == 1:
        first_days_of_month.append(all_days_within_a_year[i])

end_date_str = '2021-08-01'
end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

first_days_of_month.append(end_date)
first_days_of_month.sort()

plt.xticks(first_days_of_month)
plt.xlim((first_days_of_month[0], first_days_of_month[-1]))

# Setting date format
date_fmt = mpl_dates.DateFormatter('%b, %d %Y')
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(date_fmt)

# Setting y axis limit
plt.ylim((0,4000))

# Adding labels to graph
plt.ylabel('Price per Stock (USD)', fontsize=16)
plt.title('FAANG Companies - Closing Price Trends', fontsize=18)

# Adding legend to graph
plt.legend(title='Companies', loc=(1.01, 0.64), title_fontsize='large')

# Adjust some padding to graph
plt.tight_layout()

# Saving graph as png
plt.savefig('FAANG Stock Price.png', dpi=300)

# Showing graph as output
plt.show()
