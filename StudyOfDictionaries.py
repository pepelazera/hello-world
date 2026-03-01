student = {
    'name': 'Pedro',
    'age': 22,
    'course': 'Software engineering'
}

print(student)
print()

name = student['name']
age = student.get('age') # 22
email = student.get('email', 'not registered')

print(f"Name: {name} -- Age: {age} -- Email: {email}")
print()

if 'course' in student:
    print(f"Course: {student['course']}")
print()

student['age'] = 20
student['email'] = 'pedro@gmail.com'

print(student)

print()
student.update({'city': 'São Luís'}) # Update the dictionary and add a new specific key
course = student.pop('course') # remove and return the value

student.update({'course': 'System of information'})
print(student)

print()
last_item = student.popitem() # Remove and return the last value and key was inserted
print(last_item)
print(student)

print()
# ---------------------------------------------------------------------------------
print()

pairs = [('a', 1), ('b', 2), ('c', 3)]
dict_1 = dict(pairs)

print(dict_1) # {'a': 1, 'b': 2, 'c': 3}
