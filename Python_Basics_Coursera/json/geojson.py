import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = input('Enter the API key: ')
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

parms = {}
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

# Opening the webpage and decoding the data
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Extracting the JSON data to get the location details
json_data = json.loads(data)
lat = json_data['results'][0]['geometry']['location']['lat']
lon = json_data['results'][0]['geometry']['location']['lng']

print('Latitude of the location is:',lat)
print('Longitude of the location is:',lon)