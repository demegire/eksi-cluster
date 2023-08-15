# eksi-cluster
[Ekşisözlük](eksisozluk.com/) is the most popular Turkish social media website, which is organized like a dictionary; users create 'titles' and others write 'entries' under it like a thread. However the title (topic) might be the same for two different things, for example there is a footballer Harun Tekin and a musician Harun Tekin. Currently, users of the website report such titles to the moderation who then seperate hundreds of entries manually. We present eksicluster as a tool for automatically clustering polysemantic eksisozluk.com.

**How it Works**

It is simple.

1. Translate the entries from Turkish to English using Google Translate (unofficial API, not meant to be used commercially)
2. Convert from text to vectors using OpenAI embeddings (need to have an API key for this)
3. Cluster the vectors using k-means.

We tried directly embedding Turkish text and found out that this approach does not work well.

# Testing

**Method**

50 entries are drawn two titles that share the same name which are already manually seperated by Ekşisözlük admins. These entries are shuffled and merged into a single title which is then clustered into two clusters using our model. Below are the results.

**Results**

| Topic 1  | Topic 2 | Accuracy Score | F1 Score
| ------------- | ------------- | --------- | -------- |
| harun tekin (football player) | harun tekin (musician) | 0.94 | 0.94 |
| koray avcı (football player)  | koray avcı (musician) | 0.97 | 0.97 |
| dart | dart (programming language) | 0.57 | 0.68 |
| suskunlar (series) | suskunlar (book) | 0.96 | 0.96 |
| camel (music group) | camel (cigarette) | 0.94 | 0.93 |
| aydın | aydın (city) | 0.58 | 0.67 |

As can be seen from the results, the model is able to distinguish between sufficiently different titles with high success, but if one of the titles is a more encompassing title such as , it may be insufficient in the separation due to the pollution in the general title.
