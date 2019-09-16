#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:49:09 2019

@author: vedhoos
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the data set
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
# Converting dataset from pandas to a list of list as req by apriori
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

# Training apriori on the dataset
from apyori import apriori
# These values are mostly just arbitrarily chosen and they need to be fine-tuned empirically
rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)

# Visualising the rules
results = list(rules)
print(len(results))
print(results[0])
print(results[1])
