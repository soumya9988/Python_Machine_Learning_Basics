import json

string_of_json = '{"name": "Sofie", "is_cat" : true, "mice_caught" : 0, "feline_iq" : null}'
json_data_as_python_value = json.loads(string_of_json)
print(json_data_as_python_value)

python_data = {'name': 'Theo', 'is_dog': True, 'no_of_teeth': 6, 'no_of_pups': None}
python_value_as_json = json.dumps(python_data)
print(python_value_as_json)