# Scrope State level data from the NYT stats on github

import pandas as pd
import requests
import os
from os import getcwd

from make_graphs import make_bar_graph


# Scrape cumulative State level data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
curr_dir = getcwd()
filename = curr_dir + '/data/live/raw/State_raw.csv'
r = requests.get(url)
f = open(filename,'wb')
f.write(r.content)
f.close()
print('+/-UPDATED: ' + curr_dir + '/data/live/raw/State_raw.csv')

# Clean csv
f=pd.read_csv(filename)
keep_col = ['date','state','cases','deaths']
new_f = f[keep_col]
clean_file = new_f['date'][0] + '_State'
new_f.to_csv(curr_dir + '/data/live/clean/' + 'most_recent' + '.csv', index=False)
print('+CREATED: ' + curr_dir + '/data/live/clean/' + 'most_recent' + '.csv')
new_f.to_csv(curr_dir + '/data/live/clean/' + clean_file + '.csv', index=False)
print('+CREATED: ' + curr_dir + '/data/live/clean/' + clean_file + '.csv')

os.rename(filename, curr_dir + '/data/live/raw/' + new_f['date'][0] + '_State_raw.csv')
print('+CREATED: ' + curr_dir + '/data/live/raw/' + new_f['date'][0] + '_State_raw.csv')

# Make bar chart graph - TODO: make calls later, call fns as [clean -> graphs]
make_bar_graph(clean_file)

###--- ABOVE: LIVE
###--- BELOW: HISTORICAL

# Scrape comprehensive daily historical data
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
curr_dir = getcwd()
filename = curr_dir + '/data/historical/raw/State_final_count.csv'
r = requests.get(url)
f = open(filename,'wb')
f.write(r.content)
f.close()
print('+/-UPDATED: ' + curr_dir + '/data/historical/raw/State_final_count.csv')

# Clean

# Analytics
f=pd.read_csv(filename)
curr_date = f.iloc[-1]['date']
print(curr_date)

clean_df = f
#clean_df['d_cases'] = clean_df['cases'] - clean_df['cases'].shift(-1)

state_changes = []
for i in range(0,12004):
    if clean_df.iloc[i]['state'] not in state_changes:
        state_changes.append(clean_df.iloc[i]['state'])

# TODO:
# list for each state, then add rows from master list where state=list
# make sure to preserve date, and use commented line above with shift to find
# d_cases and d_deaths for each entry except the first entry for that state
