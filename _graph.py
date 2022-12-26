import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def histplot_count(title, df, x):
    p = sns.histplot(data=df, x=x, stat='count')
    plt.title(title)

def histplot_range_count(title, df, x, range):
    p = sns.histplot(data=df, x=x, stat='count', binrange=range)
    plt.title(title)

def show_word_cloud(text, title):
    wordcloud = WordCloud(collocations = False, background_color = 'white').generate(text)
    # Display the generated image:
    plt.figure(figsize = (10, 8), facecolor = None)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(title)
    plt.show()