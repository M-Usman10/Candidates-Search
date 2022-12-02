import json

CONFIG_FILE = "/Users/usman/PycharmProjects/TEST-WEAVIATE/configurations.json"
with open(CONFIG_FILE) as file:
    CONFIG = json.load(file)

CANDIDATE_FEATURES = {
    'about':'',
    'city':'',
    'country_code':'',
    'certifications': ['title'],
    'courses': ['title'],
    'current_company': {'name':''},
    'education': ['title','degree'],
    'education_details':'',
    'experience': [{'positions':'description','positions':'title'}, 'company'],
    'groups':'',
    'languages': ['title'],
    'name':'',
    'position':'',
    'url':''
}