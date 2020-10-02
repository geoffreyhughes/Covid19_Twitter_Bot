# Scrope State level data from the NYT stats on github

import pandas as pd
import requests
import os
from os import getcwd

from make_graphs import make_bar_graph


# Scrape State level data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
curr_dir = getcwd()
filename = curr_dir + '/data/raw/State_raw.csv'
r = requests.get(url)
f = open(filename,'w')
f.write(r.content)
f.close()

print(filename)
f=pd.read_csv(filename)

# Clean csv
keep_col = ['date','state','cases','deaths']
new_f = f[keep_col]
clean_file = new_f['date'][0] + '_State'
new_f.to_csv(curr_dir + '/data/clean/' + clean_file + '.csv', index=False)
print('+CREATED: ' + curr_dir + '/data/clean/' + clean_file + '.csv')

os.rename(filename, curr_dir + '/data/raw/' + new_f['date'][0] + '_State_raw.csv')
print('+CREATED: ' + curr_dir + '/data/raw/' + new_f['date'][0] + '_State_raw.csv')

# Make bar chart graph
make_bar_graph(clean_file)
