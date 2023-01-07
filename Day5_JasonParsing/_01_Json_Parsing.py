import json

courses = '{"name": "Abduhamid", "languages": ["Java", "Python"]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

languages_list = dict_courses['languages']
print(languages_list[0])
print(dict_courses['languages'][0])

for key in dict_courses:
    print(dict_courses[key])
