import seaborn as sns
import matplotlib.pyplot as plt

def histplot_count(title, df, x):
    p = sns.histplot(data=df, x=x, stat='count')
    plt.title(title)

def histplot_range_count(title, df, x, range):
    p = sns.histplot(data=df, x=x, stat='count', binrange=range)
    plt.title(title)