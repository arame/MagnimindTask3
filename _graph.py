import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import logging, os
from _utility import gl

save_only = True

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
    if save_only:
        fname = f"wordcloud_{title}.png"
        output_image(fname)
    else:
        plt.show()

def show_word_cloud_frequencies(term_weights, k, in_cluster_id, tag):
    wc = WordCloud(width=1200, height=800, background_color="white")
    wordcloud = wc.generate_from_frequencies(term_weights)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    fig.suptitle(f"Tag: {tag}, K: {k}, Cluster:{in_cluster_id}")
    if save_only:
        fname = f"wordcloud_{tag}_kmeans_{k}_cluster_{in_cluster_id}.png"
        output_image(fname)
    else:
        plt.show()

def plot_dict(dict_sse, title, x_label, y_label, fname):
    plt.figure(figsize = (10, 8))
    plt.plot(list(dict_sse.keys()), list(dict_sse.values()))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save_only:
        output_image(fname)
    else:
        plt.show()

def plot_silhouette_avg(dict_sse, title, x_label, y_label, tag):
    plt.figure(figsize = (10, 8))
    plt.plot(list(dict_sse.keys()), list(dict_sse.values()))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save_only:
        fname = f"elbow_plot_for_{tag}.png"
        output_image(fname)
    else:
        plt.show()

def output_image(fname):
    folder = "Images_tfidf" if gl.from_tfidf_file else "Images"
    img = os.path.join(folder, fname)
    if os.path.exists(img):
        os.remove(img)
    plt.savefig(img)
    logging.info(f"Saved image: {img}")
    plt.close()
