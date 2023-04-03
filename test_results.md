**Method**

50 entries per topic were drawn from the already separated topic (100 entries in total per topic). These entries were shuffled and re-separated through our model.
The decomposition that made by the model was compared with the actual decomposition.

**Results**

| Topic 1  | Topic 2 | Accuracy Score | F1 Score
| ------------- | ------------- | --------- | -------- |
| harun tekin (futbolcu) | harun tekin (müzisyen) | 0.94 | 0.9423076923076924 |
| koray avcı (futbolcu)  | koray avcı (şarkıcı) | 0.97 | 0.9702970297029702 |
| dart | dart (programlama dili) | 0.57 | 0.6861313868613138 |
| suskunlar (dizi) | suskunlar (kitap) | 0.96 | 0.9615384615384615 |
| camel (müzik grubu) | camel (sigara) | 0.94 | 0.9375 |
| aydın | aydın (şehir) | 0.58 | 0.676923076923077 |

As can be seen from the results, the model is able to distinguish between two completely separated titles with high success, but if one of the titles is a more general title, it may be insufficient in the separation due to the pollution in the general title.
