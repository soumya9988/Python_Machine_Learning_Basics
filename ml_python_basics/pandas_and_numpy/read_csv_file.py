import os
import pandas

print(os.listdir())

df1 = pandas.read_csv('supermarkets.csv')
print(df1)
df2 = pandas.read_json('supermarkets.json')
print(df2)
df3 = pandas.read_excel('supermarkets.xlsx', sheet_name = 0)
print(df3)
df4 = pandas.read_csv('supermarkets-commas.txt')
print(df4)
df5 = pandas.read_csv('supermarkets-semi-colons.txt', delimiter=';')
print(df5)
df6 = df5.set_index('ID', inplace=True)
print(df6)

# Label based slicing
print(df1.loc[:, 'Name'])

# index based slicing
print(df1.iloc[1:3, 1:3].values)
