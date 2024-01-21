import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def read_csv():
    return pd.read_csv("airbnb_csv.csv")


def mean_count_plot(x, y):
    df = read_csv()
    plt.figure(figsize=(8, 7))
    mean_order = df.groupby(x)[y].mean().sort_values(ascending=False).index
    counts = df[x].value_counts()
    ax = sns.barplot(x=y, y=x, data=df, estimator=np.mean, ci=None, order=mean_order)
    for i, v in enumerate(mean_order):
        ax.text(df[df[x] == v][y].mean(), i, f' Count: {counts[v]}', color='black', va='center')

    plt.title(f'Mean {y} and Counts of room by {x}')
    return plt.gcf()


def scatter(a, b):
    df = read_csv()
    df1 = df[[a, b]]
    sns.scatterplot(x=a, y=b, data=df1)
    return plt.show()
