#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:59:10 2019

@author: vedhoos
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


# Importing the data set
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values  # all rows, all col expect last
y = dataset.iloc[:, 3].values

# Splitting the dataset into train and test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 0)

# Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)"""