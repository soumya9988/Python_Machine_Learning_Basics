import pandas
from geopy.geocoders import ArcGIS
nom = ArcGIS()

dataframe = pandas.read_csv('supermarkets.csv')
dataframe['Address'] += ', ' + dataframe['City'] + ', ' + dataframe['State'] + ', ' + dataframe['Country']
dataframe['Coordinates'] = dataframe['Address'].apply(nom.geocode)
print(dataframe.Coordinates[0].latitude)

dataframe['Latitude'] = dataframe['Coordinates'].apply(lambda x: x.latitude if x is not None else None)
dataframe['Longitude'] = dataframe['Coordinates'].apply(lambda x: x.longitude if x is not None else None)
print(dataframe)
