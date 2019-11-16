import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

data_to_python = json.loads(data)
print('Name:',data_to_python['name'])
print('Phone Number:', data_to_python['phone']['number'])