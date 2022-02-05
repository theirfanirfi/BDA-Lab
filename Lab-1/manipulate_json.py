import json

# JSON string
# lab = '{"id":"9", "lab_name": "BDA", "department":"DS"}'

# # Convert string to Python dict
# labs_dict = json.loads(lab)
# print(labs_dict)
# #getting an attribute
# print(labs_dict['name'])

labs_dict = dict({
    "lab-1": {"name": "bda", "department": "DS"},
    "lab-2": {"name": "pf-e", "department": "cs"},
    "lab-3": {"name": "pf-f", "department": "se"},
})

to_json = json.dumps(labs_dict)
print(to_json)

file = open('json_data.json')
data = json.load(file)

for i in data['quiz']:
    print('Subject: ', i)
    question = data['quiz'][i]
    for q in question:
        print('Question: ', question[q]['question'])
        print('Options: ', question[q]['options'])
        print('Answer: ', question[q]['answer'])
        print('\n')
    print('\n ********************************* \n')
