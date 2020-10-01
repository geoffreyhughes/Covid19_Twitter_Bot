import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Number of cases and deaths, stacked on each other, bar graph by State
curr_dir = os.getcwd()
df=pd.read_csv(curr_dir + '/data/state_NYT_clean.csv', sep=',',header=0)
print(df)



print(df.state)
print(list(df.state))
print(list(df.cases))

df = df.sort_values('cases', ascending=False)

x_labels = list(df.state)
y_axis = list(df.cases)
y2_axis = list(df.deaths)



w = 10
nitems = len(y_axis)
x_axis = np.arange(0, nitems*w, w)

fig, ax = plt.subplots(1)

plt1 = ax.bar(x_axis, y_axis, width=w, align='center', label='Cases')
plt2 = ax.bar(x_axis, y2_axis, color='r', width=w, align='center', bottom=y_axis, label='Deaths')

# ax.set_ylabel('People')
plt.legend((plt1[0], plt2[0]), ('Cases', 'Deaths'))
ax.set_xticks(x_axis);
ax.set_xticklabels(x_labels, rotation=90);
plt.show()
