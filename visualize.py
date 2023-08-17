# Adapted from https://github.com/openai/openai-cookbook/blob/main/examples/Visualizing_embeddings_in_2D.ipynb
import numpy as np
from ast import literal_eval
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib

def visualize(df):

    matrix = np.vstack(df.embedding.values)
    tsne = TSNE(n_components = 2, perplexity = 15, random_state = 42, init='random', learning_rate = 200)
    vis_dims = tsne.fit_transform(matrix)

    colors = ["red", "blue"]
    x = [x for x, y in vis_dims]
    y = [y for x, y in vis_dims]
    color_indices = df['predicted_cluster'].values
    colormap = matplotlib.colors.ListedColormap(colors)
    plt.scatter(x, y, c=color_indices, cmap=colormap, alpha = 0.3)

    for cluster in [0,1]:
        avg_x = np.array(x)[df['predicted_cluster']==cluster].mean()
        avg_y = np.array(y)[df['predicted_cluster']==cluster].mean()
        color = colors[cluster]
        plt.scatter(avg_x, avg_y, marker = 'x', color=color, s = 100)

    plt.title("Entry Clusters Visualized Using t-SNE")

    return plt