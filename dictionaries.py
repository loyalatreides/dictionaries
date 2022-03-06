person = {
    'first_name': 'Kamran',
    'second_name': 'Habib',
    'age': '25',
    'country': 'India',
    'is_married': False,
    'skills': ['SQL','Python','MS Word','MS Powerpoint'],
    'address': {
        'street': 'Street number 5',
        'zip_code': '110025'
    }
}
print(len(person))
print(person['first_name'])
print(person['age'])
print(person['country'])
print(person['skills'])

print(person.get('is_married'))
print(person.get('address'))
person['hobbies'] = ['Reading','Coding','Football']
print(person)
person['skills'].append('HTML')
print(person)
person['country']='Netherlands'
print(person)
print('first_name' in person)
#person.pop('is_married')
#print(person)
#person.popitem()
#print(person)
#print(person.items())
#print(person.clear())
#del person
#print(person)
person_1 = person.copy()
print(person_1)
keys = person.keys()
print(keys)
values = person.values()
print(values)

#Exersice
#1
dog = {}
print(dog)
#2
dog = {
    'name': 'Auralius',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': '4',
    'age': '8'
}
print(dog)
#3
student = {
    'first_name': 'Kamran',
    'last_name': 'Habib',
    'gender': 'Male',
    'age': '25',
    'marital status': 'Single',
    'skills': ['HTML','PHP','Python','SQL','Jupyter'],
    'country': 'India',
    'city': 'New Delhi',
    'address': 'Abul Fazal Enclave'
}
print(student)
#4
print(len(student))
#5
#values = student.values('skills')
#print(values)
#6
student['skills'] = 'MS Office', 'MongoDB'
print(student)
key = student.keys()
print(key) #7
value = student.values()
print(value) #8
print(student.items()) #9
del student['first_name'] #10
print(student)
del student #11
