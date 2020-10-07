import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from pdf2image import convert_from_path



# Number of cases and deaths, stacked on each other, bar graph by State
def make_bar_graph(clean_file):

    # Read in file made in scrape_NYT.py
    curr_dir = os.getcwd()
    df = pd.read_csv(curr_dir + '/data/live/clean/' + clean_file + '.csv', sep=',',header=0)

    # Sort the df by descending case values; assign lists for each axis
    df = df.sort_values('cases', ascending=False)

    w = 10
    x_labels = list(df.state)
    y_axis = list(df.cases)
    y2_axis = list(df.deaths)
    nitems = len(y_axis)
    x_axis = np.arange(0, nitems*w, w)

    fig, ax = plt.subplots(1)

    plt1 = ax.bar(x_axis, y_axis, width=w, align='center', label='Cases')
    plt2 = ax.bar(x_axis, y2_axis, color='r', width=w, align='center', bottom=y_axis, label='Deaths')

    plt.legend((plt1[0], plt2[0]), ('Cases', 'Deaths'))
    plt.suptitle('Cumulative COVID-19 Cases and Deaths in the United States', fontsize=14)
    ax.set_xticks(x_axis);
    ax.set_xticklabels(x_labels, rotation=90, fontsize=8)

    plt.tight_layout()
    plt.subplots_adjust(top=0.89)

    plt.savefig(curr_dir + '/data/live/graphs/' + clean_file + '_bar_graph.pdf', format='pdf', )
    print('+CREATED: ' + curr_dir + '/data/live/graphs/' + clean_file + '_bar_graph.pdf')

    images = convert_from_path(curr_dir + '/data/live/graphs/' + clean_file + '_bar_graph.pdf', 500)

    for image in images:
        image.save(curr_dir + '/data/live/graphs/' + clean_file + '_bar_graph.png', 'PNG')
        print('+CREATED: ' + curr_dir + '/data/live/graphs/' + clean_file + '_bar_graph.png')
        image.save(curr_dir + '/data/live/graphs/' + 'most_recent_bar_graph.png', 'PNG')
        print('+CREATED: ' + curr_dir + '/data/live/graphs/' + 'most_recent_bar_graph.png')


# # Percentage increase in cases
# def
