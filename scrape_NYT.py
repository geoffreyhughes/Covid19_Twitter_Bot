# Scrope State level data from the NYT stats on github

import pandas as pd
import requests
from os import getcwd

from make_graphs import make_bar_chart

# TODO: County level data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv"

curr_dir = getcwd()
filename = curr_dir + '/data/county_NYT.csv'
r = requests.get(url)

f = open(filename,'w')
f.write(r.content)
f.close()
print(filename)



# Scrape State level data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
curr_dir = getcwd()
filename = curr_dir + '/data/state_NYT.csv'
r = requests.get(url)
f = open(filename,'w')
f.write(r.content)
f.close()

print(filename)
f=pd.read_csv(filename)

# Clean csv
keep_col = ['date','state','cases','deaths']
new_f = f[keep_col]
clean_file = new_f['date'][0] + '_State_NYT'
new_f.to_csv(curr_dir + '/data/' + clean_file + '.csv', index=False)

# Make bar chart graph
make_bar_chart(clean_file)
