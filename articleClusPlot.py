import matplotlib.pyplot as plt
import numpy

plt.figure()

counts = {11: 78, 7: 55, 3: 52, 4: 52, 12: 39, 9: 35, 18: 35, 8: 33, 14: 29, 19: 29, 2: 28, 5: 28, 6: 28, 1: 24, 0: 20, 10: 20, 13: 14, 17: 12, 16: 11, 15: 9}
clus_counts = [counts[i] for i in range(20)]


plt.bar(range(20), clus_counts)

plt.xlabel('Cluster Number')
plt.ylabel('Number of Stories per Cluster')
plt.title('Semantic Story Content Clustering (Sample Size: 631 Aug. 2012 articles)')

##highlight a couple of bars 
plt.bar(7, clus_counts[7], color='y')
plt.bar(0, clus_counts[0], color='g')

