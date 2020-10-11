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
num_rows = len(clean_df)
#clean_df['d_cases'] = clean_df['cases'] - clean_df['cases'].shift(-1)

states = []
for i in range(0,num_rows):
    if clean_df.iloc[i]['state'] not in states:
        states.append(clean_df.iloc[i]['state'])

# Dictionary storing a list for each State
state_cases = {}
state_deaths = {}
for state in states:
    state_cases[state] = []
    state_deaths[state] = []

# Add cases and deaths to cooresponding list
for i in range(0,num_rows):
    state_cases[clean_df.iloc[i]['state']].append(clean_df.iloc[i]['cases'])
    state_deaths[clean_df.iloc[i]['state']].append(clean_df.iloc[i]['deaths'])


# Pad a zero for each state's first entry d_cases and d_deaths calculations
for state in states:
    state_cases[state].insert(0,0)
    state_deaths[state].insert(0,0)


# Note: May have been able to do this entire process a less complicated way?
# Without dictionaries. Maybe by sorting the df by State first, date second.

print(state_cases['California'])
print(state_deaths['California'])

# Add column of changes for each row, except for the first entry
for i in range(num_rows-1,0,-1):
    clean_df.loc[i, 'd_cases'] = state_cases[clean_df.iloc[i]['state']][-1] - state_cases[clean_df.iloc[i]['state']][-2]
    state_cases[clean_df.iloc[i]['state']].pop(-1)
    clean_df.loc[i, 'd_deaths'] = state_deaths[clean_df.iloc[i]['state']][-1] - state_deaths[clean_df.iloc[i]['state']][-2]
    state_deaths[clean_df.iloc[i]['state']].pop(-1)


    # if location is first of its state list: do % change compared to 10+ prev entries

clean_df.to_csv(curr_dir + '/data/historical/clean/' + 'covid_master_list' + '.csv', index=False)



# ax1 = df_pct_change.plot.scatter(x='date',
#                       y='width',
#                       c='DarkBlue')




# TODO:
# list for each state, then add rows from master list where state=list
# make sure to preserve date, and use commented line above with shift to find
# d_cases and d_deaths for each entry except the first entry for that state
