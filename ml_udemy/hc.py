#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:03:26 2019

@author: vedhoos
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the data set using pandas
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

# Using dendogram to find optimum no of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method= 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()

# Ftting HC to the mall dataset.
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_hc == 0,0], X[y_hc == 0,1], s =100, c= 'red', label = 'Careful')
plt.scatter(X[y_hc == 1,0], X[y_hc == 1,1], s =100, c= 'blue', label = 'Standard')
plt.scatter(X[y_hc == 2,0], X[y_hc == 2,1], s =100, c= 'green', label = 'Target')
plt.scatter(X[y_hc == 3,0], X[y_hc == 3,1], s =100, c= 'cyan', label = 'Careless')
plt.scatter(X[y_hc == 4,0], X[y_hc == 4,1], s =100, c= 'magenta', label = 'Sensible')
plt.title('Clusters of clients')
plt.xlabel('Annual income(k$)')
plt.ylabel('Spending score(1-100)')
plt.legend()
plt.show()
