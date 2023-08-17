import sys
import asyncio
import numpy as np
from sklearn.cluster import KMeans

from scrape import get_topic
from translate import translate
from embedder import embed
from visualize import visualize

async def cluster_topic(topic_name, n_clusters, start_page, end_page, df=None):

    # Get topic entries unless a df is provided for testing purposes
    if df is None:
        df = await get_topic(topic_name, start_page, end_page) # get_topic(topic name, start page, end page)

    # Translate
    df["translation"] = df['entry'].apply(translate)

    # Get embeddings
    df = embed(df)
    matrix = np.vstack(df.embedding.values)
    
    # Cluster
    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
    kmeans.fit(matrix)
    labels = kmeans.labels_
    df["predicted_cluster"] = labels
    
    return df   


async def main():

    if len(sys.argv) != 5:
        raise Exception('Invalid input. Wrap the topic in \'quotation marks\' if it is not a single word. Example usage: \n python main.py mit 3 1 5 ')

    # Arguments
    topic_name = sys.argv[1]
    n_clusters = int(sys.argv[2])
    start_page = int(sys.argv[3])
    end_page =  int(sys.argv[4])

    df = await cluster_topic(topic_name, n_clusters, start_page, end_page)

    plt = visualize(df)
    plt.show()

    df = df.drop(columns=['embedding'])
    print(df.head())
    print('Cluster Distribution: ')
    print(df['predicted_cluster'].value_counts())

    df.to_csv('data/{}.csv'.format(topic_name.replace(" ", "_")), index = False, encoding = 'utf-8')

    return

if __name__ == "__main__":
    asyncio.run(main())