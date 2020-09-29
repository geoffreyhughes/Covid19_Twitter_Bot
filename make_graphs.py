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

x_labels = list(df.state)
y_axis = list(df.cases)

w = 10
nitems = len(y_axis)
x_axis = np.arange(0, nitems*w, w)

fig, ax = plt.subplots(1)
ax.bar(x_axis, y_axis, width=w, align='center')
ax.set_xticks(x_axis);
ax.set_xticklabels(x_labels, rotation=90);
plt.show()
