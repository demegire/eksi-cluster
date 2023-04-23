# eksi-cluster
Tool for clustering polysemantic eksisozluk.com page entries

**To Do**

- [x] clustering
- [x] validation
- [ ] text processing to get rid of scraping artifacts

**Method**

50 entries per topic were drawn from the already separated topic (100 entries in total per topic). These entries were shuffled and re-separated through our model.
The decomposition that made by the model was compared with the actual decomposition.

**Results**

| Topic 1  | Topic 2 | Accuracy Score | F1 Score
| ------------- | ------------- | --------- | -------- |
| harun tekin (football player) | harun tekin (musician) | 0.94 | 0.9423076923076924 |
| koray avcı (football player)  | koray avcı (musician) | 0.97 | 0.9702970297029702 |
| dart | dart (programming language) | 0.57 | 0.6861313868613138 |
| suskunlar (series) | suskunlar (book) | 0.96 | 0.9615384615384615 |
| camel (music group) | camel (cigarette) | 0.94 | 0.9375 |
| aydın | aydın (city) | 0.58 | 0.676923076923077 |

As can be seen from the results, the model is able to distinguish between two completely separated titles with high success, but if one of the titles is a more general title, it may be insufficient in the separation due to the pollution in the general title.
