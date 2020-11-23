#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import title, xlim


def read_file(f):
    reader = csv.reader(f, dialect="excel");

    colleges = []

    for college in reader:
        if not college or college[0] == "":
            continue
        colleges.append([college[0]] + [int(x) for x in college[1:-1]] + [float(college[-1])])

    colleges.sort(key=lambda x: x[-1])

    return colleges



def make_plot(colleges):
    START_YEAR = 2006
    END_YEAR = len(colleges[0]) - 2 + START_YEAR
    fig = plt.figure(dpi=120, figsize=(10,8))
    # plt.subplots(constrained_layout=True)

    XLIM = (START_YEAR, END_YEAR - 1)
    YLIM = (len(colleges), 0)

    title_font = {
        'fontsize': "small",
        'color': "black",
        "font": "Ubuntu",
    }


    for i in range(len(colleges)):
        college = colleges[i]
        axes = plt.subplot(7, 5, i + 1)
        axes.set_facecolor("#EEE")
        axes.set_xlim(XLIM)
        axes.set_ylim(YLIM)
        axes.grid(True, "both", "both", color="white")
        axes.set_yticks(range(30, 0, -10))
        axes.set_xticks([2010, 2015])

        if i % 5 != 0:
            axes.set_yticklabels([])

        if len(colleges) - i >= 6:
            axes.set_xticklabels([])

        axes.set_title(college[0], fontdict=title_font)
        axes.plot(range(START_YEAR, END_YEAR), college[1:-1], color="black")

    plt.subplots_adjust(hspace=0.6, wspace=0.1)

    fig.savefig("plot.png")

with open("norrington_raw.csv", "r") as f:
    colleges = read_file(f)
    make_plot(colleges)
    # plt.show()