# Scrope State level data from the NYT stats on github

import pandas as pd
import requests
from os import getcwd

# TODO: County level data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv"

directory = getcwd()
filename = directory + '/data/county_NYT.csv'
r = requests.get(url)

f = open(filename,'w')
f.write(r.content)
f.close()
print(filename)



# Scrape State level data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
directory = getcwd()
filename = directory + '/data/state_NYT.csv'
r = requests.get(url)
f = open(filename,'w')
f.write(r.content)
f.close()

print(filename)
f=pd.read_csv(filename)

# Clean csv
keep_col = ['date','state','cases','deaths']
new_f = f[keep_col]
new_f.to_csv(directory + '/data/' + new_f['date'][0] + '_live_State_NYT_clean.csv', index=False)
