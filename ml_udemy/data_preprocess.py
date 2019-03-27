import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer

# Importing the data set
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values # Take all the rows, all columns expect the last one
y = dataset.iloc[:, 3].values

# Taking care of missing data
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0,)
