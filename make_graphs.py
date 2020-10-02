import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def make_bar_chart(clean_file):

    # Number of cases and deaths, stacked on each other, bar graph by State
    curr_dir = os.getcwd()
    df=pd.read_csv(curr_dir + '/data/' + clean_file + '.csv', sep=',',header=0)
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
    plt.suptitle('Cumulative COVID-19 Cases and Deaths in the United States', fontsize=16)
    ax.set_xticks(x_axis);
    ax.set_xticklabels(x_labels, rotation=90, fontsize=8)

    plt.tight_layout()
    plt.subplots_adjust(top=0.89)

    plt.savefig(curr_dir + '/data/graphs/' + clean_file + '_bar_graph.pdf')
