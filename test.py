import asyncio
import pandas as pd
from sklearn.metrics import f1_score

from scrape import get_topic
from main import cluster_topic
from visualize import visualize

async def main():
    
    df_1 = await get_topic('harun tekin (futbolcu)', 1, 5) # First cluster
    df_2 = await get_topic('harun tekin (müzisyen)', 1, 5) # Second cluster

    df_1["real_cluster"] = 0
    df_2["real_cluster"] = 1

    df_merged = pd.concat([df_1, df_2])
    df_merged = df_merged.sample(frac = 1)

    df_merged = await cluster_topic('placeholder', 2, 0, 0, df_merged)
    
    plt = visualize(df_merged)
    plt.show()
    
    df_merged = df_merged.drop(columns=['embedding'])
    df_merged.to_csv('data/test.csv', index = False, encoding = 'utf-8')
    label_1 = input('Please inspect the csv manually now and input the label for the first cluster as it appears in predicted_cluster: ')
    if int(label_1): # Discrepancy
        df_merged["predicted_cluster"] = abs(df_merged["predicted_cluster"] - 1) # Invert values

    f1 = f1_score(df_merged["real_cluster"], df_merged["predicted_cluster"])
    f1_alternative = f1_score(df_merged["real_cluster"], abs(df_merged["predicted_cluster"] - 1))

    print('F1 Score: {:.2f}'.format(f1))
    print('... or if you got the label wrong it could be: {:.2f}'.format(f1_alternative))
    print('Cluster Distribution: ')
    print(df_merged['predicted_cluster'].value_counts())

    return f1

if __name__ == "__main__":
    asyncio.run(main())