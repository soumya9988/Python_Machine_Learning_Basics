#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:55:34 2019

@author: vedhoos
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

# Importing the data set
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values  # all rows, all col expect last
y = dataset.iloc[:, 4].values

# Encoding categorical data: Converting it to numerical values
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
# Creating the dummy variables.
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap
X = X[: , 1:]

# Splitting the dataset into train and test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 0)

# Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)"""

# Fitting the MLR to the training set
regressor = LinearRegression()

# Predicting the test set result
y_pred = regressor.predict(X_test)

# Building the optimum model using the Backward Elimination
X = np.append(arr= np.ones((50, 1)).astype(int), values= X , axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_ols = sm.OLS(endog= y, exog = X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0, 1, 2, 4, 5]]
regressor_ols = sm.OLS(endog= y, exog = X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0, 1, 4, 5]]
regressor_ols = sm.OLS(endog= y, exog = X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0, 1, 4]]
regressor_ols = sm.OLS(endog= y, exog = X_opt).fit()
regressor_ols.summary()







