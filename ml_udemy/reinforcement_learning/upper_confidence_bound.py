#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:28:01 2019

@author: vedhoos
"""

# importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt, log

# importing the data set
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# implementing the UCB
N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0] * d  # Creating a vector of size d with value 0
sums_of_rewards = [0] * d
total_reward = 0

for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i]/ numbers_of_selections[i]
            delta_i = sqrt(3/2 * log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] += 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] += reward
    total_reward += reward

"""
print('Ads selected', ads_selected)
print('Number of selection', numbers_of_selections)
print('Sum of rewards', sums_of_rewards)
print(total_reward)
"""

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

