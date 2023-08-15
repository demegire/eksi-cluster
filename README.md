# eksi-cluster

[Ekşisözlük](eksisozluk.com/) is the most popular Turkish social media website, which is organized like a dictionary; users create 'titles' and others write 'entries' under it like a thread. However the title (topic) might be homonymous, for example there is a footballer Harun Tekin and a musician Harun Tekin. Currently, users of the website [report](https://eksisozluk1923.com/baslik-ayrimi-onerileri--5556790) such titles to the moderation who then seperate hundreds of entries manually. We present eksicluster as a tool for automatically clustering these titles. Clustering is not only useful for this purpose, feel free to play with this tool and maybe find new uses.

**Usage**

main.py takes in 4 arguments:

1. Title name such as `mit` or `'im westen nichts neues'`. Make sure to wrap the title in quotes if there are multiple words in it.
2. Number of clusters. If you think there are 2 distinct notions in a title, you might still go for 3 to weed out unrelated stuff.
3. First relevant page. Acceptable range: 1, last page - 1
4. Last relevant page. Acceptable range: 2, last page

```
python main.py mit 3 1 18
```

A 'title name'.csv will be saved in data/ containing the Turkish entries, the translated entries and the cluster labels.

test.py is useful for validating the performance of this tool. You can use the already seperated titles to get an F1 score on that dataset. To do this change the name of the titles in the script and the number of pages to be evaluated. The script supports 2 titles.  

```
python test.py
```

A test.csv will be saved in data/ containing the Turkish entries, the translated entries, the real labels and the cluster labels.


**How it Works**

eksi-cluster is simple.

1. Translate the entries from Turkish to English using Google Translate (unofficial API, not meant to be used commercially)
2. Convert from text to vectors using OpenAI embeddings (need to have an API key for this)
3. Cluster the vectors using k-means.

We tried directly embedding Turkish text and found out that this approach does not work well.

# Testing

**Method**

50 entries are drawn two titles each that share the same name which are already manually seperated by Ekşisözlük admins. These entries are then merged into a single title which is clustered into two. Below are the results.

**Results**

| Topic 1  | Topic 2 | Accuracy Score | F1 Score
| ------------- | ------------- | --------- | -------- |
| harun tekin (football player) | harun tekin (musician) | 0.92 | 0.92 |
| koray avcı (football player)  | koray avcı (musician) | 0.97 | 0.97 |
| dart | dart (programming language) | 0.57 | 0.68 |
| suskunlar (series) | suskunlar (book) | 0.96 | 0.96 |
| camel (music group) | camel (cigarette) | 0.94 | 0.93 |
| aydın | aydın (city) | 0.58 | 0.67 |

As can be seen from the results, the tool is able to distinguish between sufficiently different titles with high accuracy, but if one of the titles is a more encompassing title such as dart, it may be insufficient in the separation due to the variety of information in that title.
