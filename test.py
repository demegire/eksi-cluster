import asyncio
import pandas as pd
import numpy as np
import openai

from scrape import get_topic
from translate import translate
from embedder import embedderEksi
from sklearn.cluster import KMeans



async def main():
    
    #loop = asyncio.get_event_loop()
    df = await get_topic('harun tekin (futbolcu)',1,2)
    df_2 = await get_topic('harun tekin (müzisyen)',1,2)
    df["label"] = 0
    df_2["label"] = 1
    df = df.append(df_2,ignore_index=True)
    df['translation'] = df['entry']

    for i in range(len(df)):
        df.iloc[i, 2] = translate(df.iloc[i,0])
    df = embedderEksi(df)
    matrix = np.vstack(df.embedding.values)
    
    # clustering
    
    n_clusters = 2

    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
    kmeans.fit(matrix)
    labels = kmeans.labels_
    df["Cluster"] = labels
    df.drop(columns=['embedding'],inplace=True)
    df.to_csv('data/{}.csv'.format('harun_tekin'),index=False,encoding='utf-8')

    return df

asyncio.run(main())