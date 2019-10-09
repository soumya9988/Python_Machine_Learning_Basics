#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:46:53 2019

@author: vedhoos
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Importing the data set
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values  # all rows, all col expect last
y = dataset.iloc[:, 1].values

# Splitting the dataset into train and test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3,
                                                    random_state = 0)

# Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)"""

# Fitting Simple linear regression to training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the test set
y_pred = regressor.predict(X_test)

# Visualising the training set result
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary Vs. Experience(Training Set)')
plt.xlabel('Years of Exp.')
plt.ylabel('Salary')
plt.show()

# Visualising the test set result
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary Vs. Experience(Test Set)')
plt.xlabel('Years of Exp.')
plt.ylabel('Salary')
plt.show()